# Discord Macro Board - Complete with Animated OLED Display
# KMK Firmware for XIAO RP2040

import board
import busio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

# ============ OLED SETUP ============
try:
    i2c = busio.I2C(board.D7, board.D6)  # SCL=D7, SDA=D6
    import adafruit_ssd1306
    from PIL import Image, ImageDraw, ImageFont
    
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    oled_available = True
except:
    oled_available = False
    print("OLED not found - continuing without display")

# ============ GLOBAL VARIABLES ============
mute_status = False
volume_level = 50
last_button_press = ""
button_press_time = 0
animation_frame = 0

# ============ OLED DISPLAY FUNCTIONS ============
def draw_startup_animation():
    """Animated Discord circle startup"""
    if not oled_available:
        return
    
    image = Image.new('1', (128, 64))
    draw = ImageDraw.Draw(image)
    
    # Draw animated circle expanding
    for frame in range(5):
        image = Image.new('1', (128, 64))
        draw = ImageDraw.Draw(image)
        radius = 5 + (frame * 3)
        draw.ellipse([(64-radius, 32-radius), (64+radius, 32+radius)], outline=255)
        display.image(image)
        display.show()
        time.sleep(0.1)

def draw_main_display():
    """Display main status with animations"""
    if not oled_available:
        return
    
    global animation_frame
    animation_frame = (animation_frame + 1) % 20
    
    image = Image.new('1', (128, 64))
    draw = ImageDraw.Draw(image)
    
    # Top bar - animated border
    border_y = 12
    draw.line([(0, border_y), (128, border_y)], fill=255, width=1)
    
    # Status line 1: Microphone status
    mic_icon = "🎤" if mute_status else "🔊"
    mic_text = "MIC: OFF" if mute_status else "MIC: ACTIVE"
    draw.text((5, 18), mic_text, fill=255)
    
    # Animated pulsing indicator for mute status
    pulse = abs((animation_frame % 10) - 5) // 2
    draw.ellipse([(120-pulse, 20-pulse), (125+pulse, 25+pulse)], outline=255)
    
    # Status line 2: Volume level
    vol_bar_width = int((volume_level / 100) * 80)
    draw.rectangle([(5, 32), (85, 38)], outline=255)
    draw.rectangle([(5, 32), (5+vol_bar_width, 38)], fill=255)
    draw.text((90, 32), f"{volume_level}%", fill=255)
    
    # Status line 3: Last action
    if button_press_time > 0 and time.time() - button_press_time < 2:
        draw.text((5, 45), f"Action: {last_button_press}", fill=255)
        # Animated checkmark
        if animation_frame % 10 < 5:
            draw.text((120, 45), "✓", fill=255)
    else:
        draw.text((5, 45), "Ready", fill=255)
    
    display.image(image)
    display.show()

# ============ KEYBOARD SETUP ============
keyboard = KMKKeyboard()

# Define GPIO pins for switches
PINS = [
    board.D26,  # SW1 - Mute Mic
    board.D27,  # SW2 - Leave Call
    board.D28,  # SW3 - Camera On/Off
    board.D29,  # SW4 - Screen Share
]

# Set up key scanner
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Add encoder support
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.encoders.append((board.D2, board.D1, None))

# Define keyboard layout
keyboard.keymap = [
    [
        KC.MUTE,                    # SW1
        KC.LCTRL(KC.ALT(KC.D)),     # SW2
        KC.LCTRL(KC.SHIFT(KC.M)),   # SW3
        KC.LCTRL(KC.SHIFT(KC.S)),   # SW4
    ]
]

# ============ KEY PRESS CALLBACK ============
def on_key_press(key):
    """Update display when button is pressed"""
    global mute_status, last_button_press, button_press_time
    
    button_press_time = time.time()
    
    if key == KC.MUTE:
        mute_status = not mute_status
        last_button_press = "MUTE" if mute_status else "UNMUTE"
    elif key == KC.LCTRL(KC.ALT(KC.D)):
        last_button_press = "LEAVE"
    elif key == KC.LCTRL(KC.SHIFT(KC.M)):
        last_button_press = "CAMERA"
    elif key == KC.LCTRL(KC.SHIFT(KC.S)):
        last_button_press = "SCREEN"

# Override process_key to track presses
original_process = keyboard.process_key
def tracked_process(key, is_pressed):
    if is_pressed:
        on_key_press(key)
    return original_process(key, is_pressed)
keyboard.process_key = tracked_process

# ============ ENCODER CALLBACK ============
def encoder_callback(keyboard, direction, accel_time):
    global volume_level, last_button_press, button_press_time
    
    if direction == 1:  # Clockwise
        volume_level = min(100, volume_level + 5)
        keyboard.send(KC.VOLU)
    else:  # Counter-clockwise
        volume_level = max(0, volume_level - 5)
        keyboard.send(KC.VOLD)
    
    last_button_press = "VOLUME"
    button_press_time = time.time()

encoder_handler.callbacks.append(encoder_callback)

# ============ STARTUP ============
draw_startup_animation()
time.sleep(0.5)

# ============ MAIN LOOP ============
def update_display_task():
    """Update OLED display constantly"""
    while True:
        draw_main_display()
        time.sleep(0.1)

# Start keyboard
if __name__ == "__main__":
    import threading
    
    # Start display update thread
    if oled_available:
        display_thread = threading.Thread(target=update_display_task, daemon=True)
        display_thread.start()
    
    keyboard.go()

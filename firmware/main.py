import time
import board
import digitalio
import rotaryio
import neopixel
import busio
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import usb_hid

# ---------- USB HID ----------
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# ---------- PINS (XIAO RP2040) ----------
# Buttons
PIN_MUTE        = board.GP26
PIN_LEAVE_CALL  = board.GP27
PIN_CAMERA      = board.GP28
PIN_SHARE       = board.GP29

# Encoder
PIN_ENC_A       = board.GP6
PIN_ENC_B       = board.GP7
PIN_ENC_BTN     = board.GP0

# LEDs (SK6812)
PIN_LEDS        = board.GP3
NUM_LEDS        = 2

# OLED I2C
PIN_OLED_SCL    = board.GP4
PIN_OLED_SDA    = board.GP2
OLED_WIDTH      = 128
OLED_HEIGHT     = 32

# ---------- BUTTON SETUP ----------
def make_button(pin):
    b = digitalio.DigitalInOut(pin)
    b.switch_to_input(pull=digitalio.Pull.UP)  # active low
    return b

btn_mute       = make_button(PIN_MUTE)
btn_leave      = make_button(PIN_LEAVE_CALL)
btn_camera     = make_button(PIN_CAMERA)
btn_share      = make_button(PIN_SHARE)
btn_enc        = make_button(PIN_ENC_BTN)

# Last states for edge detection
last_mute = last_leave = last_camera = last_share = last_enc = True

# ---------- ROTARY ENCODER ----------
encoder = rotaryio.IncrementalEncoder(PIN_ENC_A, PIN_ENC_B)
last_position = encoder.position

# ---------- NEOPIXELS ----------
pixels = neopixel.NeoPixel(PIN_LEDS, NUM_LEDS, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)

def set_status_leds(mic_on, cam_on):
    # LED0 = mic status, LED1 = camera status
    pixels[0] = (0, 255, 0) if mic_on else (255, 0, 0)   # green = on, red = muted
    pixels[1] = (0, 255, 255) if cam_on else (255, 0, 255)

# ---------- OLED ----------
i2c = busio.I2C(PIN_OLED_SCL, PIN_OLED_SDA)
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

def oled_status(mic_on, cam_on, sharing, volume):
    oled.fill(0)
    oled.text(f"Mic:   {'ON'  if mic_on else 'MUTE'}", 0, 0, 1)
    oled.text(f"Cam:   {'ON'  if cam_on else 'OFF'}", 0, 10, 1)
    oled.text(f"Share: {'ON'  if sharing else 'OFF'}", 0, 20, 1)
    # Very rough volume display
    oled.text(f"Vol: {volume}", 70, 20, 1)
    oled.show()

# ---------- STATE ----------
mic_on = True
cam_on = True
sharing = False
volume_level = 50  # just for display, 0–100

set_status_leds(mic_on, cam_on)
oled_status(mic_on, cam_on, sharing, volume_level)

# ---------- HELPER: SEND SHORTCUTS ----------
# Change these key combos to match your Discord hotkeys
def send_mute_toggle():
    # Example: Ctrl+Shift+M
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)

def send_leave_call():
    # Example: Ctrl+Shift+H (set this in Discord keybinds)
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.H)

def send_camera_toggle():
    # Example: Ctrl+Shift+V
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.V)

def send_share_toggle():
    # Example: Ctrl+Shift+S
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.S)

# ---------- MAIN LOOP ----------
while True:
    # ----- Buttons (edge detect, active low) -----
    now_mute   = btn_mute.value
    now_leave  = btn_leave.value
    now_cam    = btn_camera.value
    now_share  = btn_share.value
    now_encbtn = btn_enc.value

    # Mute button
    if last_mute and not now_mute:
        send_mute_toggle()
        mic_on = not mic_on
        set_status_leds(mic_on, cam_on)
        oled_status(mic_on, cam_on, sharing, volume_level)
    last_mute = now_mute

    # Leave call
    if last_leave and not now_leave:
        send_leave_call()
        # You might want to reset states here if you like
    last_leave = now_leave

    # Camera toggle
    if last_cam and not now_cam:
        send_camera_toggle()
        cam_on = not cam_on
        set_status_leds(mic_on, cam_on)
        oled_status(mic_on, cam_on, sharing, volume_level)
    last_camera = now_cam

    # Screen share
    if last_share and not now_share:
        send_share_toggle()
        sharing = not sharing
        oled_status(mic_on, cam_on, sharing, volume_level)
    last_share = now_share

    # Encoder button: also mute toggle (like a push-to-mute)
    if last_enc and not now_encbtn:
        send_mute_toggle()
        mic_on = not mic_on
        set_status_leds(mic_on, cam_on)
        oled_status(mic_on, cam_on, sharing, volume_level)
    last_enc = now_encbtn

    # ----- Rotary for volume -----
    position = encoder.position
    if position != last_position:
        delta = position - last_position
        last_position = position

        if delta > 0:
            # clockwise = volume up
            for _ in range(delta):
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                volume_level = min(100, volume_level + 2)
        elif delta < 0:
            # counter-clockwise = volume down
            for _ in range(-delta):
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                volume_level = max(0, volume_level - 2)

        oled_status(mic_on, cam_on, sharing, volume_level)

    time.sleep(0.01)

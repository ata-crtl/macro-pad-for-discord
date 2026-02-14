# Discord Macro Keyboard

A customdesigned discordmacro keyboard with complete PCB design. Features include ,discord shortcut keys for quick messaging and commands during gameplay or streaming.

## Why I Made This Project

I created this discord macro keyboard to streamline my discord experience during gaming sessions and streaming. Having dedicated physical buttons for common discord commands removes the need to alt-tab or memorize  keyboard shortcuts  allowing me to stay focused in-game while maintaining communication with my team and Community.

# Bill of Materials (BOM)

Ataullah Macro Pad - Discord Control Deck

| Qty | Component | Part Number | Description | Link/Notes |
|-----|-----------|-------------|-------------|-----------|
| 1 | Seeed XIAO RP2040 | - | Unsoldered microcontroller board | [Seeed Wiki](https://wiki.seeedstudio.com/XIAO-RP2040/) |
| 4 | MX-Style Switches | - | Mechanical keyboard switches for macro keys (SW1-SW4) | Mechanical switch footprint compatible |
| 2 | EC11 Rotary Encoder | EC11 | Push-button rotary encoder for volume control | Hackaday/Aliexpress |
| 20 | 1N4148 Diode | 1N4148 | Through-hole protection diodes | Standard component |
| 1 | OLED Display | SSD1306 | 0.91" 128x32 I²C OLED display (GND-VCC-SCL-SDA) | [Seeed Store](https://www.seeedstudio.com/) |
| 16 | SK6812 MINI-E LED | SK6812MINI-E | Addressable RGB LEDs (2 on PCB, rest for future) | **Important: Use MINI-E, not standard SK6812** |
| 16 | DSA Keycaps | - | White blank keycaps for MX switches | Standard 1u keycaps |
| 4 | M3x16mm Screw | - | Case assembly fasteners | Stainless steel |
| 4 | M3x5mmx4mm Heat-set Insert | - | Threaded inserts for 3D-printed case | [AliExpress Example](https://www.aliexpress.us/item/2255800046543591.html) |

## Key Notes
- **LED Footprint:** Must be SK6812 **MINI-E** (not standard SK6812 mini)
- **OLED Pin Order:** GND-VCC-SCL-SDA (critical - verify PCB matches)
- **Total Key Capacity:** Designed for 4 keys + 1 encoder, but can support up to 16 keys with additional switches
- **All parts are from the official Hackpad approved kit**

## Sources
- Hackpad Approved Parts: https://blueprint.hackclub.com/hackpad/parts
- Component datasheets available in `/datasheets` folder



<img width="1227" height="800" alt="image" src="https://github.com/user-attachments/assets/5e1e26c7-61e9-4c83-a89f-01a7db8b9be1" />
<img width="720" height="511" alt="image" src="https://github.com/user-attachments/assets/612d8d1a-6c2c-45e0-ac80-5f8755db5c5f" />


<img width="1372" height="751" alt="image" src="https://github.com/user-attachments/assets/ccf9ca14-e554-41a5-a248-8f0c2fd4a439" />








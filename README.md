# Discord Macro Board

A compact macro keyboard designed specifically for Discord voice calls. Four programmable buttons, a rotary encoder, and an OLED display make it easy to control your Discord experience without reaching for your keyboard.

## What It Does

I wanted a quick way to mute myself, leave calls, and toggle video without hunting for the right Discord hotkey. This board does exactly that.

- **Mute button** - instantly toggle mic on/off
- **Leave call button** - one-touch call exit
- **Camera toggle** - switch video on/off  
- **Screen share button** - quick sharing control
- **Rotary encoder** - adjust volume by turning the knob
- **OLED display** - shows what's happening in real-time

## The Build

**Electronics:**
- Seeed XIAO RP2040 microcontroller
- 4 MX-style mechanical switches
- EC11 rotary encoder
- SSD1306 128x64 OLED display
- 2 SK6812 RGB addressable LEDs

**Case:**
- 3D printed bottom and top
- M3 screws and heatset inserts for assembly

## What I Learned

- PCB design is a lot of trial and error with routing
- OLED displays are surprisingly fun to program
- 3D printing tolerance matters - I had to file some holes bigger
- KMK firmware is way easier than QMK for simple projects

## Parts List

See BOM.md for full component list and part numbers.

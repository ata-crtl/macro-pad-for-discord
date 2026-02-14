# Discord Macro Keyboard

A customdesigned discordmacro keyboard with complete PCB design. Features include ,discord shortcut keys for quick messaging and commands during gameplay or streaming.

## Why I Made This Project

I created this discord macro keyboard to streamline my discord experience during gaming sessions and streaming. Having dedicated physical buttons for common discord commands removes the need to alt-tab or memorize  keyboard shortcuts  allowing me to stay focu# What You'll Need - Shopping List 🛒

# Discord Macro Keyboard

A custom-designed Discord macro keyboard featuring 12 programmable keys for quick Discord commands, built around the approved Seeed XIAO RP2040 microcontroller. Perfect for gaming and streaming sessions.

## Why I Made This Project

I created this Discord macro keyboard to streamline my Discord experience during gaming sessions and streaming. Having dedicated physical buttons for common Discord commands eliminates the need to alt-tab or memorize complex keyboard shortcuts, allowing me to stay focused in-game while maintaining communication with my team and community.

## How to Use This Project

The keyboard features programmable macro keys that can be customized to send pre-defined Discord messages, emojis, or commands. Simply:
1. Connect the keyboard via USB-C cable
2. Install QMK firmware (provided in repository)
3. Press any key to send the programmed macro
4. Use QMK Configurator to customize macros as needed

## 3D Model

![Full 3D CAD assembly showing the complete Discord keyboard design with all components](3D_MODEL_IMAGE_URL)

## PCB Design

![PCB layout with all traces, components, and mounting points for Discord macro keyboard](PCB_IMAGE_URL)

## Wiring Diagram

![Complete wiring diagram showing connections between XIAO RP2040, switches, and components](WIRING_DIAGRAM_URL)

## Bill of Materials (BOM)

| Part | Quantity | Description | Unit Price (£) | Total (£) | Source | Direct Link |
|------|----------|-------------|----------------|-----------|--------|-------------|
| **Seeed XIAO RP2040** | 1 | Approved microcontroller, QMK compatible, RP2040 @ 133MHz | £7.00 | £7.00 | The Pi Hut | [Buy Here](https://thepihut.com/products/seeed-xiao-rp2040) |
| **Gateron Red Switches** | 12 | Linear gaming switches, 45g actuation, smooth operation | £0.85 | £10.20 | SerpentKeys UK | [Buy Here](https://www.serpentkeys.co.uk/collections/switches) |
| **PBT Keycaps (Cherry Profile)** | 12 | Durable double-shot PBT keycaps, matte finish | £1.20 | £14.40 | CustomKeyCaps UK | [Buy Here](https://www.customkeycaps.co.uk) |
| **PCB + Stencil** | 1 | 2-layer custom PCB with castellated pads | £8.50 | £8.50 | JLCPCB | [Order Here](https://jlcpcb.com/) |
| **1N4148 Diodes (DO-35)** | 12 | Signal diodes for keyboard matrix | £0.13 | £1.56 | Switch Electronics | [Buy Here](https://www.switchelectronics.co.uk/products/1n4148-small-signal-diode-100v-150ma-pack-of-10) |
| **2.2kΩ Resistors (0805)** | 10 | Pull-up resistors for keyboard matrix | £0.05 | £0.50 | Amazon UK | [Buy Here](https://www.amazon.co.uk) |
| **0.1µF Capacitors (0805)** | 2 | Decoupling capacitors for stable power | £0.08 | £0.16 | Amazon UK | [Buy Here](https://www.amazon.co.uk) |
| **RGB LED (WS2812B)** | 1 | Addressable RGB LED for underglow effects | £1.50 | £1.50 | The Pi Hut | [Buy Here](https://thepihut.com) |
| **M2x6mm Screws & Nuts** | 4 sets | Mounting hardware for case | £0.30 | £1.20 | Amazon UK | [Buy Here](https://www.amazon.co.uk) |
| **USB-C Cable (1m)** | 1 | USB-C to USB-A cable, Anker brand | £4.99 | £4.99 | Amazon UK | [Buy Here](https://www.amazon.co.uk) |
| **3D Printed Case** | 1 | Custom enclosure (PLA, self-printed or service) | £4.00 | £4.00 | 3DPrintUK | [Order Here](https://www.3dprint-uk.co.uk) |
| **3M VHB Tape** | 1 roll | Double-sided mounting tape for PCB | £2.50 | £2.50 | Amazon UK | [Buy Here](https://www.amazon.co.uk) |

### **Total Project Cost: £56.95**

*(Prices may vary based on quantity discounts, shipping, and supplier availability)*

---

## Project Files Included

- `BOM.csv` - Complete bill of materials with part links and prices
- `discord_keyboard.f3d` - Fusion 360 source design file
- `discord_keyboard.step` - STEP format 3D model (electronics included)
- `discord_keyboard.kicad_pro` - KiCad project file
- `discord_keyboard.sch` - Schematic file
- `gerbers.zip` - Gerber files for PCB manufacturing
- `firmware/` - All QMK firmware source code and compiled .hex files
- `README.md` - This documentation
- `images/` - All screenshots and diagrams

## Design Features

- ✅ **Fully custom CAD assembly** with all electronics integrated
- ✅ **Original design** (not a copy of any existing guide)
- ✅ **Complete PCB layout** with proper routing and castellated pad connections
- ✅ **QMK firmware included** with keymap customization
- ✅ **Approved Seeed XIAO RP2040** microcontroller
- ✅ **Sanity-checked** with another maker
- ✅ **STEP file with all electronics** ready for Blueprint submission

## Technical Specifications

- **Microcontroller:** Seeed XIAO RP2040 (ARM Cortex-M0+ @ 133MHz)
- **Keyboard Layout:** 12-key matrix (3x4)
- **Connectivity:** USB-C (native HID support)
- **Firmware:** QMK with custom keymap
- **Dimensions:** 80mm x 60mm x 20mm
- **Weight:** ~45g
- **Power:** 5V USB, <100mA
- **Additional Features:** RGB underglow, tactile feedback, compact design

---

**Project Status:** Design complete and ready for Blueprint submission

---

*Created for Blueprint - Hack Club hardware project submission*





<img width="1227" height="800" alt="image" src="https://github.com/user-attachments/assets/5e1e26c7-61e9-4c83-a89f-01a7db8b9be1" />
<img width="720" height="511" alt="image" src="https://github.com/user-attachments/assets/612d8d1a-6c2c-45e0-ac80-5f8755db5c5f" />


<img width="1372" height="751" alt="image" src="https://github.com/user-attachments/assets/ccf9ca14-e554-41a5-a248-8f0c2fd4a439" />








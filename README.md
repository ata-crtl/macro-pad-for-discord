# Discord Macro Keyboard

A customdesigned discordmacro keyboard with complete PCB design. Features include ,discord shortcut keys for quick messaging and commands during gameplay or streaming.

## Why I Made This Project

I created this discord macro keyboard to streamline my discord experience during gaming sessions and streaming. Having dedicated physical buttons for common discord commands removes the need to alt-tab or memorize  keyboard shortcuts  allowing me to stay focu# What You'll Need - Shopping List 🛒

**Build your own Discord Macro Pad!** A tiny 4-button + rotary knob control deck that makes Discord way more convenient.

---

## The Shopping List

| How Many | What You're Getting | Part Code | Details | Price | Where to Find It |
|----------|-------------------|-----------|---------|-------|-----------------|
| 1 | **XIAO RP2040 Brain** | XIAO-RP2040 | The tiny microcontroller that runs everything | £10-13 | [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) or [ThePiHut](https://thepihut.com/products/seeed-xiao-rp2040) |
| 4 | **Mechanical Switches** | - | The clicky buttons for your macro keys | £0.80-£2.50 each (£3.20-£10 total) | [CustomKeyboardsUK](https://customkeyboardsuk.co.uk/collections/cherry-mx-switches) or [MechBoards](https://mechboards.co.uk/) |
| 1 | **Volume Knob (Rotary Encoder)** | EC11 | Twist it to control volume, press it to mute | £2.50-£4.00 | [Pimoroni](https://shop.pimoroni.com/products/ec11-rotary-encoder-module) or [RobotShop](https://uk.robotshop.com/products/ec11-rotary-encoder-module) |
| 20 | **Protection Diodes** | 1N4148 | These protect your switches (you won't need all 20, but good to have spares) | £0.50-£1.50 | [Amazon UK](https://www.amazon.co.uk/s?k=1n4148+diode) |
| 1 | **Tiny Screen** | SSD1306 | 0.91" OLED display to show what you're doing | £3.00-£5.00 | [SB Components](https://shop.sb-components.co.uk/products/0-91-inch-oled-display-breakout) or [Amazon UK](https://www.amazon.co.uk/s?k=0.91+oled+ssd1306) |
| 2 | **RGB LEDs** | SK6812MINI-E | Tiny colourful LEDs (make sure it's the MINI-E version!) | £0.30-£0.50 each (£0.60-£1.00 total) | [Etsy UK](https://www.etsy.com/uk/listing/1564895619/sk6812-mini-e-rgb-led-100pcs-for) |
| 4 | **Keycaps** | - | The white plastic tops that go on your buttons | £0.50-£1.50 each (£2-£6 total) | [Amazon UK](https://www.amazon.co.uk/s?k=dsa+keycaps+white) |
| 4 | **Screws** | M3x16mm | For holding your case together | £0.20-£0.40 each (£0.80-£1.60 total) | [Amazon UK](https://www.amazon.co.uk/s?k=m3+16mm+screw) or [Screwfix](https://www.screwfix.com/) |
| 4 | **Case Inserts** | M3 Heat-set | Threaded bits for your 3D-printed case | £0.15-£0.25 each (£0.60-£1.00 total) | [Vector3D](https://vector3d.shop/products/heat-set-insert-m3-standard) (cheapest bulk option) |

---

## How Much Will It Cost? 💷

| Budget Option | Fast Option |
|---|---|
| **£23-35 total** | **£35-45 total** |
| Shop on AliExpress (takes 2-3 weeks) | Buy from UK shops (delivers in days) |
| Order everything from China | Mix of Amazon UK + specialist shops |
| **Good for:** Saving money | **Good for:** You're impatient |

**Realistic estimate:** Around **£30-40** for most people.

---

## What Button Does What? 🎮

This is set up for Discord, but you can change it however you like:

| Button | What It Does | You Press |
|--------|-------------|-----------|
| **Top-Left (SW1)** | Mute your microphone | 1 click = toggle mute on/off |
| **Top-Right (SW2)** | Leave the call | Press once to leave |
| **Bottom-Left (SW3)** | Turn your camera on/off | 1 click = toggle camera |
| **Bottom-Right (SW4)** | Start/stop screen sharing | Press to share your screen |
| **Twist the Knob** | Control your volume | Clockwise = louder, counter-clockwise = quieter |
| **Press the Knob** | Mute/unmute | Same as the top-left button |

---

## Important Things to Remember ⚠️

1. **The LEDs have a specific version** - Make sure you buy **SK6812 MINI-E**, not just "SK6812 mini". It's the smaller one and it's the right size for your board.

2. **The screen has a specific pin order** - Your OLED needs to have pins in this order: **GND-VCC-SCL-SDA**. Check before you buy! Some have them mixed up and won't work.

3. **You'll need to program it** - The firmware is already written for you (CircuitPython), but you'll need to upload it to the XIAO using a USB cable.

4. **The 3D case isn't included** - You'll need to 3D print the case yourself (or buy one pre-made). The heat-set inserts are for mounting it.

---

## Different Ways to Save Money 💰

### **If you want it ASAP (5-7 days):**
Buy from UK shops like Amazon UK, ThePiHut, Pimoroni. You'll spend a bit more but it arrives quickly.
**Est. £35-45**

### **If you have time (2-3 weeks):**
Order everything from AliExpress and wait for it to ship from China. Way cheaper but slower.
**Est. £23-35**

### **Smart Middle Ground:**
Buy the expensive stuff (XIAO, OLED) from UK shops for speed, and get the cheap bits (LEDs, switches) from AliExpress to save money.
**Est. £28-38**

---

## Where These Parts Come From 🌍

All of these are from the **official Hackpad kit** - so you know they'll work together. If you want to swap anything out, that's fine, but stick to these specs:

- ✅ [Full list of approved Hackpad parts](https://blueprint.hackclub.com/hackpad/parts)

---

## Need the Technical Stuff? 🔧

If you want datasheets or more info:
- [XIAO RP2040 Docs](https://wiki.seeedstudio.com/XIAO-RP2040/)
- [LED Datasheet](https://cdn.shopify.com/s/files/1/2612/7473/files/SK6812MINI-E_REV_v1.1_EN.pdf)
- [OLED Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)

---

## Quick Shopping Links (Copy & Paste Ready)

**Budget Build (AliExpress):**
- XIAO: Search "XIAO RP2040"
- LEDs: Search "SK6812 MINI-E"
- Switches: Search "MX mechanical switches"
- Encoder: Search "EC11 rotary encoder"

**Fast Build (UK):**
- XIAO: [ThePiHut](https://thepihut.com/products/seeed-xiao-rp2040)
- Switches: [MechBoards](https://mechboards.co.uk/)
- OLED: [Amazon UK](https://www.amazon.co.uk/s?k=0.91+oled+ssd1306)
- Encoder: [Pimoroni](https://shop.pimoroni.com/products/ec11-rotary-encoder-module)

---

**Questions?** Check the repo's README or ask in the Hack Club Discord! 🚀
sed in-game while maintaining communication with my team and Community.




<img width="1227" height="800" alt="image" src="https://github.com/user-attachments/assets/5e1e26c7-61e9-4c83-a89f-01a7db8b9be1" />
<img width="720" height="511" alt="image" src="https://github.com/user-attachments/assets/612d8d1a-6c2c-45e0-ac80-5f8755db5c5f" />


<img width="1372" height="751" alt="image" src="https://github.com/user-attachments/assets/ccf9ca14-e554-41a5-a248-8f0c2fd4a439" />








## Doppler Radar Golf Tracker: Idiot's Guide to Setup

This is a step-by-step guide to connecting and setting up your HB100 Doppler radar, amplifier, and Raspberry Pi to track golf clubhead speed.

---

### 🧱 Step 1: Mount the HB100 Radar Module

1. Take your **HB100 radar module** out of the packaging.
2. Mount it using zip ties, Velcro, or tape to a plastic bracket or box.
3. Ensure the radar face is aimed **perpendicular** to your clubhead's swing direction (down-the-line or face-on).

> 📌 Tip: Do NOT block the front of the radar with metal or thick wood. Acrylic, foam, or air is fine.

---

### 🔌 Step 2: Power the HB100

1. Connect **VCC** on the HB100 to a **12V power source** (e.g., wall adapter or step-up module).
2. Connect **GND** to the power supply ground.
3. Leave the **IF (intermediate frequency) output** unconnected for now — this is the signal we'll amplify.

> 📌 Tip: If using a step-up converter (e.g., MT3608), connect its input to 5V and output to 12V (tune using a voltmeter).

---

### 🔧 Step 3: Connect the Op-Amp (LM358)

1. Connect the **IF output** from HB100 to the **non-inverting input** (+) of the op-amp.
2. Set up gain resistors (e.g., 1kΩ and 100kΩ for \~100x gain).
3. Connect op-amp **output** to Channel 0 (CH0) of the **MCP3008 ADC**.
4. Power the op-amp with **5V** from the Pi and connect **GND**.

> 📌 Tip: You can use a breakout board version of LM358 to avoid soldering.

---

### 🧠 Step 4: Connect the MCP3008 to Raspberry Pi

Wire the MCP3008 like this:

| MCP3008 Pin | Raspberry Pi GPIO   |
| ----------- | ------------------- |
| VDD, VREF   | 3.3V                |
| AGND, DGND  | GND                 |
| CLK         | GPIO11 (SPI0\_SCLK) |
| DOUT        | GPIO9 (SPI0\_MISO)  |
| DIN         | GPIO10 (SPI0\_MOSI) |
| CS/SHDN     | GPIO8 (SPI0\_CE0)   |
| CH0         | From Op-Amp Output  |

> Enable SPI via `sudo raspi-config` → Interface Options → SPI → Yes

---

### 🧪 Step 5: Run the Code and Collect Data

1. Boot up your Raspberry Pi and make sure Python is installed.
2. Use the sample code from the Doppler Radar Code file.
3. Run the script:

```bash
python3 radar_capture.py
```

4. Swing a club through the radar field and watch the FFT plot.
5. You should see a peak in frequency — this corresponds to clubhead speed!

> 📌 Tip: If signal is weak, increase op-amp gain or check radar aim.

---

### ✅ Final Checklist

-

You're now tracking swing speed using microwave radar!

Let me know if you want to add range estimation, position tracking, or Wi-Fi-based swing data streaming next.


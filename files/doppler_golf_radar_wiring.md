## Doppler Radar Golf Swing Tracker - Part 2: Wiring Diagram

### A. HB100 to Op-Amp

- **HB100 Connections**:
  - VCC → 12V regulated power
  - GND → Ground
  - IF (intermediate frequency output) → Op-Amp non-inverting input (+)

- **Op-Amp**:
  - Gain configured via resistor network (example: 1k/10k for ~100x gain)
  - Output of Op-Amp → MCP3008 CH0 input
  - Powered by 5V from Raspberry Pi

---

### B. MCP3008 to Raspberry Pi GPIO (SPI Wiring)

| MCP3008 Pin | Raspberry Pi GPIO |
|-------------|-------------------|
| VDD, VREF   | 3.3V              |
| AGND, DGND  | GND               |
| CLK         | GPIO11 (SPI0_SCLK)|
| DOUT        | GPIO9 (SPI0_MISO) |
| DIN         | GPIO10 (SPI0_MOSI)|
| CS/SHDN     | GPIO8 (SPI0_CE0)  |
| CH0         | From Op-Amp Output|

> Note: Enable SPI on the Pi via `raspi-config` → Interface Options → SPI → Enable


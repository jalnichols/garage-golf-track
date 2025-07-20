## Doppler Radar Golf Swing Tracker - Part 1: Parts List (Raspberry Pi Version)

### 🛒 Required Components

| Item | Suggested Model | Qty | Notes |
|------|------------------|-----|-------|
| **Raspberry Pi 4** | Pi 4 Model B (4GB or 8GB) | 1 | Go with 4GB unless you want headroom for other projects |
| **MicroSD Card (32GB+)** | SanDisk Extreme 32GB UHS-I | 1 | For Raspberry Pi OS |
| **Raspberry Pi Power Supply** | Official 5V 3A USB-C | 1 | Stable power is critical |
| **10.525 GHz Radar Module** | HB100 Microwave Sensor | 1–2 | ~$5–$10 each on Amazon, eBay, AliExpress |
| **Op-Amp Module** | LM358, TLV2372, or similar on breakout board | 1 | For signal amplification (or build your own with resistors) |
| **Analog-to-Digital Converter (ADC)** | MCP3008 10-bit SPI ADC | 1 | Well-supported by Pi; 8 channels if you add sensors later |
| **Breadboard** | Half-size or full-size | 1 | For quick prototyping |
| **Jumper wires (male-male)** | 40-pack Dupont wires | 1 | Connect HB100, op-amp, ADC, Pi |
| **12V DC Power Adapter** | 12V 1A + barrel jack | 1 | Powers HB100 separately |
| **Step-up Converter (optional)** | MT3608 or similar 5V → 12V | 1 | Only needed if you want to power HB100 from Pi |
| **Plastic enclosure** | Acrylic or PET project box | 1 | Non-metallic enclosure for radar face |
| **Tripod or mount** | Ball head camera mount or 3D printed | 1 | To aim at swing plane (face-on/down-line) |
| **(Optional) USB Oscilloscope** | Hantek 6022BE or similar | 1 | Helpful for tuning signal amplification |


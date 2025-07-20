# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Doppler radar golf swing tracker project using a Raspberry Pi and HB100 10.525 GHz radar module. The system captures Doppler shift signals from golf ball movement and calculates ball velocity using FFT analysis.

## Architecture

### Hardware Components
- **HB100 Radar Module**: 10.525 GHz microwave sensor for Doppler detection
- **Raspberry Pi 4**: Main processing unit running the Python signal processing
- **MCP3008 ADC**: Converts analog radar signals to digital via SPI interface
- **Op-Amp Circuit**: Amplifies the weak IF output from HB100 (~100x gain)

### Signal Processing Chain
1. HB100 detects moving golf ball and outputs intermediate frequency (IF) signal
2. Op-amp amplifies the weak signal 
3. MCP3008 ADC digitizes the amplified signal at ~10 kHz sampling rate
4. Python script performs FFT analysis to find peak Doppler frequency
5. Converts Doppler shift to velocity using wavelength calculation (λ ≈ 0.0285m for 10.525 GHz)

### Key Files
- `files/ddoppler_golf_radar_code.py`: Main signal processing script using SPI, NumPy FFT, and matplotlib
- `files/doppler_golf_radar_parts.md`: Complete parts list and component specifications
- `files/doppler_golf_radar_wiring.md`: SPI wiring diagram between Pi, MCP3008, and radar module

## Development Commands

### Running the Radar System
```bash
python files/ddoppler_golf_radar_code.py
```

### Dependencies
The Python script requires:
- `spidev` - SPI interface library
- `numpy` - FFT calculations and array processing  
- `matplotlib` - Signal visualization
- `time` - Sampling timing control

### Hardware Setup
- Enable SPI on Raspberry Pi: `raspi-config` → Interface Options → SPI → Enable
- HB100 requires 12V power supply (separate from Pi)
- MCP3008 uses SPI0 interface (GPIO 8-11)
- Op-amp powered from Pi 5V rail

## Signal Processing Details

The core algorithm samples the radar IF output at 10 kHz for 2000 samples, removes DC bias, performs FFT analysis to find the peak Doppler frequency, and converts to ball velocity using the formula: `velocity = (doppler_freq * wavelength) / 2`

The system is designed to measure golf ball velocities typically in the 50-200 mph range during swing analysis.
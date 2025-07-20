# Doppler Radar Golf Swing Tracker - Part 3: Python Signal Processing Example

import spidev
import numpy as np
import matplotlib.pyplot as plt
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1_000_000

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    val = ((adc[1] & 3) << 8) + adc[2]
    return val

# Collect 2000 samples at ~10 kHz
samples = []
start = time.time()
while len(samples) < 2000:
    val = read_adc(0)
    samples.append(val)
    time.sleep(0.0001)  # ~10 kHz

elapsed = time.time() - start
print(f"Collected {len(samples)} samples in {elapsed:.2f}s")

# Convert to numpy array
signal = np.array(samples) - np.mean(samples)
fs = len(samples) / elapsed

# FFT
fft_vals = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1/fs)

# Find peak frequency (ignore DC)
peak_idx = np.argmax(fft_vals[1:]) + 1
peak_freq = freqs[peak_idx]
doppler_shift = peak_freq

# Convert to velocity (HB100 wavelength ≈ 0.0285 m)
velocity_mps = (doppler_shift * 0.0285) / 2
velocity_mph = velocity_mps * 2.23694

print(f"Peak Doppler: {doppler_shift:.1f} Hz → {velocity_mph:.1f} mph")

# Plot
plt.plot(freqs, fft_vals)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Doppler Spectrum")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
from rtlsdr import *
import math

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sample_rate = sdr.sample_rate
sdr.center_freq = 4.22e6
center_freq = sdr.center_freq
sdr.gain = 4

NumberOfSamples = 256*math.floor(sample_rate*.1/256)
samples = sdr.read_samples(NumberOfSamples)
sdr.close()

time_axis = np.linspace(0, NumberOfSamples/sample_rate, int(NumberOfSamples))
plt.plot(time_axis/1e-3, samples.real, 'g')
plt.plot(time_axis/1e-3, samples.imag, 'r')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

plt.show()

X = fft(samples)
N = len(X)
n = np.arange(N)
T = N/sample_rate
freq = n/T

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')

plt.show()

# plt.show()

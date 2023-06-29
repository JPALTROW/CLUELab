import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
from rtlsdr import *
import math

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sample_rate = sdr.sample_rate
sdr.center_freq = 4.22e6 #should be set to desired frequency
center_freq = sdr.center_freq
sdr.gain = 4
Time = 10.0 # ms (can be decimal)

#CHANGE NUMBER OF SAMPLES USING TIME
NumberOfSamples = 256*math.floor(sample_rate*Time/(256*1000)) #number of samples must be a multiple of 256
samples = sdr.read_samples(NumberOfSamples) #read in data
sdr.close()

#Plot data
#Time domain first
time_axis = np.linspace(0, NumberOfSamples/sample_rate, int(NumberOfSamples))
plt.plot(time_axis/1e-3, samples.real, 'g')
plt.plot(time_axis/1e-3, samples.imag, 'r')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

plt.show()

#FFT to have Frequency Domain Second
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

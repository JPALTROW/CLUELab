from pylab import *
import numpy as np
from numpy.fft import fft, ifft
from rtlsdr import * #There were some issues using this on Windows, may need to use WSL or something?
import math

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sample_rate = sdr.sample_rate
sdr.center_freq = 4e6 #should be set to desired frequency
center_freq = sdr.center_freq
sdr.gain = 40.2
sdr.set_direct_sampling(2)
f = open("output.txt", "w")



#CHANGE NUMBER OF SAMPLES USING TIME
NumberOfSamples = 100*256
samples = sdr.read_samples(NumberOfSamples) #read in data
sdr.close()
#Clean first 0.8 ms of data
samples = samples[int(0.8*sample_rate/1000):]
NumberOfSamples-=int(0.8*sample_rate/1000)


for i in samples:
    f.write(str(i)+"\n")
f.close()

#Plot data
#Time domain first
time_axis = np.linspace(0, NumberOfSamples/sample_rate, int(NumberOfSamples))
plot(time_axis/1e-3, samples.real, 'g')
plot(time_axis/1e-3, samples.imag, 'r')
xlabel('Time (ms)')
ylabel('Amplitude')

show()

# FFT to have Frequency Domain Second
psd(samples, NFFT=1024, Fs=sample_rate/1e6, Fc=center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')

show()

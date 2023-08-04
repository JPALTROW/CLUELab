from pylab import *
import numpy as np
from numpy.fft import fft, ifft
from rtlsdr import * #There were some issues using this on Windows, may need to use WSL or something?
import math


sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sample_rate = sdr.sample_rate
sdr.center_freq = 28.134e6 #should be set to desired frequency
center_freq = sdr.center_freq
sdr.gain = 40.1

f = open("output.txt", "w")
#CHANGE NUMBER OF SAMPLES
NumberOfSamples = 10000*256
samples = sdr.read_samples(NumberOfSamples) #read in data
sdr.close()
#Clean first 0.8 ms of data
samples = samples[int(0.8*sample_rate/1000):]
NumberOfSamples-=int(0.8*sample_rate/1000)


def get_samp(show_plot = False):


    for i in samples.real:
        f.write(str(i)+"\n")
    f.close()
    if(show_plot):
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

def cross_corr():
    sample_corr = []
    print(sample_rate/(2*center_freq))
    for i in range(NumberOfSamples):
        if (i % 0.3 < (0.5 * (sample_rate/2*center_freq))):
            sample_corr.append(1.0)
        else:
            sample_corr.append(-1.0)

    time_axis = np.linspace(0, NumberOfSamples/sample_rate, int(NumberOfSamples))
    plot(time_axis/1e-3, sample_corr, 'g')
    xlabel('Time (ms)')
    ylabel('Amplitude')

    show()
# cross_corr()
get_samp(True)

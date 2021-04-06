import scipy.fftpack as fourier

gn = [0,1,2,3,4]
gk = fourier.fft(gn)
print(abs(gk))
import numpy as np
from scipy import signal as sg
from scipy import fft
from matplotlib import pyplot as plt
L = 100
n = np.arange(0,L)
Fs = 200
Ts = 1/Fs
F1 = 10
F2 = 20
t = n*Ts
x1 = np.sin(2*np.pi*F1*t)
x2 = np.sin(2*np.pi*F2*t)
x = x1 + x2
plt.plot(t,x1+x2)
plt.show()

N = 128
Xf = fft.fft(x,N)

Xm = np.linspace(-Fs)

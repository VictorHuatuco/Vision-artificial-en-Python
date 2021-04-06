import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

f = 400
Wn = f*2*np.pi
N = 2

b2, a2 = signal.iirfilter(N, Wn, btype = "lowpass",analog = True,ftype= "butter")
Ws2,Hs2 = signal.freqs(b2,a2)

WsHz2 = Ws2/(2*np.pi)

plt.plot(WsHz2,abs(Hs2),label = "|H(s)| con N = 1")
plt.legend()
plt.xlabel("Frecuencia Hz")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
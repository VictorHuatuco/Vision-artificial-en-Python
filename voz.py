import pyaudio as pa 
import matplotlib.pyplot as plt
import numpy as np 
import struct
import scipy.fftpack as fourier
a = pa.PyAudio()

FRAMES = 1024*8
FORMATO = pa.paInt16
CANAL = 1
Fs = 4410 

stream = a.open(
    format = FORMATO,
    channels = CANAL,
    rate = Fs,
    input = True,
    output = True,
    frames_per_buffer = FRAMES
    )

#Creamos grafica

fig ,(ax, ax1) = plt.subplots(2) 
aud_x = np.arange(0,FRAMES,1)
x_fft = np.linspace(0,Fs,FRAMES)
line, = ax.plot(aud_x,np.zeros(FRAMES))
line_fft, = ax1.semilogx(x_fft, np.zeros(FRAMES))
ax.set_ylim(-3,3)
ax1.set_xlim(1,5000)
fig.show()

while True:
    data = stream.read(FRAMES)
    dataInt = struct.unpack(str(FRAMES) + "h",data)
    yx = np.asarray(dataInt)
    ymax = np.max(yx)
    ymin = np.min(yx)
    yx = (2*(yx - ymin)/(ymax - ymin))-1
    line.set_ydata(yx)
    M = abs(fourier.fft(dataInt))
    ax1.set_ylim(0,np.max(M))
    line_fft.set_ydata(M)

    fig.canvas.draw()
    fig.canvas.flush_events()

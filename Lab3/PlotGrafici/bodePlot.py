#Leonardo Pasquato
#Bode plot and sperimental misures in the same diagram
#bastieme

import numpy as np
import matplotlib.pyplot as plt
import control
import math
import warnings
warnings.filterwarnings('ignore')

R = math.pow(10,3) 
C = math.pow(10,-8)
L = 500*math.pow(10,-3)

a = R*C
b = L*C
c = R*C
d = 1
#transfer function {jw = s}
G = control.tf([a, 0], [b, c, d])
print(G)

#points magnitude
x = 2*math.pi
ax = [100*x, 1000*x, 2000*x, 2500*x, 3000*x, 5000*x, 10000*x, 50000*x]
ay = [0.031, 0.38, 2.24, 2.3, 1.108, 0.396, 0.163, 0.01]
dby = [1,1,1,1,1,1,1,1]
for i in range(8):
    #transform mesures from Volt to deciBel
    dby[i] = dby[i] * 20 * math.log10(ay[i]/5)

#plot magnitude and phase
mag,phase,omega = control.bode(G,Hz=False,dB=True,deg=False,grid=True)

#points phase
fx = [100*x, 1000*x, 2000*x, 2500*x, 3000*x, 5000*x, 10000*x, 50000*x]
fy = [2.68, 0.364, 0.017, 0.011, 0.02, 0.068, 0.0192, 0.0058]
rady = [1,1,1,1,1,1,1,1]
for j in range(8):
    rady[j] = rady[j] * math.atan(-(1/R)*(fx[j]*L - (1/(fx[j]*C))))

ax1 = plt.subplot(211)
plt.scatter(ax,dby, color = 'red', marker=(5, 2))
plt.tick_params('x', labelsize=6)

ax2 = plt.subplot(212, sharex=ax1)
phaseCentered = phase + x
plt.plot(omega,phaseCentered)
plt.scatter(fx,rady, color = 'green', marker=(5, 2))

plt.xlabel('Frequenza angolare (rad/s)')
plt.ylabel('Phase (rad)')
plt.xscale('log')
plt.show()

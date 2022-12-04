#plot caso sottosmorzato
import numpy as np
import matplotlib.pyplot as plt
import math

#plt.xlabel("Tempo (s)")
#plt.ylabel("Tensione (V)")

R = math.pow(10,4)
C = math.pow(10, -9)
L = 500 * math.pow(10, -3)

alpha = 100
omegazero2 = 1/(L * C)
omegad = math.sqrt(omegazero2 - math.pow(alpha, 2))
B1 = 2.5
B2 = (alpha * B1) / (omegad)

px = [0.0032, 0.0081, 0.0151, 0.023, 0.0312]
py = [0.8, -0.36, 0.2, -0.06, 0.06]

x = np.linspace(0., 0.032, 1000)
xa = x
ya = 2.5 * np.exp(-100*xa)

ytot = ya * np.cos(43588 * (xa / 100) -0.13)

plt.figure()
plt.scatter(px,py, marker = (5, 2), color = 'green')
plt.plot(xa, ya, '--r')
plt.plot(xa, ytot)
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')

#plot axis
axx = np.linspace(0., 0.032, 1000)
axy = axx * 0
plt.plot(axx, axy, color = 'black')


plt.show()

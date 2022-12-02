#plot caso sottosmorzato
import numpy as np
import matplotlib.pyplot as plt
import math

plt.xlabel("Tempo (s)")
plt.ylabel("Tensione (V)")

def f(x):
   return 2,5 * np.exp(-10000 * x) * np.cos(44721 * x - 0.225)

x = np.linspace(-10, 10, 100)

plt.plot(x, f(x), color='red')

plt.show()

plt.show()
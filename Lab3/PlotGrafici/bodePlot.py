
import numpy as np
import matplotlib.pyplot as plt
import control
import math

import warnings
warnings.filterwarnings('ignore')

#G = control.tf([0.32*.00001,0],[0.1024*0.0000000005,0.32*0.00001,1])
G = control.tf([0.00001, 0], [0.0000000005, 0.00001, 1])
print(G)

#w = np.logspace(-math.pi/2,math.pi/2)
mag,phase,omega = control.bode(G,Hz=False,dB=True,deg=False)

plt.show()


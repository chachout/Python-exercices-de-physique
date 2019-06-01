from scipy import*
from scipy.integrate import odeint
import scipy.integrate as integr 
from math import exp

import matplotlib.pyplot as plt

t=linspace(0,50,50)

def equa(v,t):
    return 59.4696*((np.exp(t/6.0673)-1)/(np.exp(t/6.0673)+1))

sol =integr.odeint(equa,0,t)

plt.plot(t, sol)
plt.grid()
plt.ylabel("position (en m)")
plt.xlabel("temps (en s)")
plt.title("Position en fonction du temps")

plt.show()
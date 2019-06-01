import matplotlib.pyplot as plt
from scipy.optimize import *
import numpy as np
T=np.array([0,7,18,27,37,56,102])
C=np.array([34.83,32.14,28.47,25.74,23.14,18.54,11.04])
f=lambda x : sum((C-C[0]*np.exp(-T*x))**2)
df=lambda x : 2*C[0]*sum(T*(C-C[0]*np.exp(-T*x))*np.exp(-T*x))
ddf=lambda x : 2*C[0]*sum(T**2 * (2*C[0]*np.exp(-x*T)-C) * np.exp(-x*T))
knewton=newton(df,0.02,ddf)
print("k selon Newton",knewton)
kdicho=bisect(df,0.005,0.02)
print("k selon dichotomie",kdicho)
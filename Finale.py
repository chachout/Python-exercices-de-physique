import matplotlib.pyplot as plt
from scipy.optimize import 
import numpy as np
T=np.array([0,7,18,27,37,56,102])
C=np.array([34.83,32.14,28.47,25.74,23.14,18.54,11.04])
f=lambda x : sum((C-C[0]*np.exp(-T*x))**2)
fv=np.vectorize(f)
A=0.1
X=np.linspace(0,A,100)
Y=fv(X)
plt.plot(X,Y)
plt.show()
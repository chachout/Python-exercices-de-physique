
import numpy as np
import scipy.integrate as integr
import matplotlib.pyplot as plt

R=10*(10**3)
Q=5.0*(10**-3)
C=1.0*(10**-3) 
T=R*C
def equation1(q,t):
    return -q/(R*C)
X= np.linspace(-2*T,8*T,1000)

Y = integr.odeint(equation1,Q,X)

plt.subplot(2,1,1)

plt.grid()
plt.title("Variation de l'intensité")
plt.axvline(x=T,color='b')
plt.text(T-0.5,-0.05,r'$\tau$',color='r')
plt.plot(X,1000*Y/T,color='r',lw=4)
plt.grid()
plt.xlabel("temps (en secondes)")
plt.ylabel("courant (en mA)")

plt.subplot(2,1,2)


plt.xlabel("temps (en secondes)")
plt.ylabel("charge (en mC)")
plt.title("Variation de la charge")
plt.axvline(x=T,color='g')
plt.text(T-0.5,-0.25,r'$\tau$',color='r')
plt.plot(X,1000*Y,color='y',lw=4)

plt.draw()
plt.show()
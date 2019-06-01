import matplotlib.pyplot as plt
import numpy as np
T=np.array([0,7,18,27,37,56,102])
C=np.array([34.83,32.14,28.47,25.74,23.14,18.54,11.04])
Ordre1 = np.log(C/C[0])
plt.title("vérification ordre 1")
plt.plot(T,Ordre1,"o")
plt.plot(T,-0.011214*T)
plt.xlabel("temps",fontsize=20)
plt.ylabel("ln(Cexp/C0) et y=-0.011214x",fontsize=20)
plt.grid()
plt.show()
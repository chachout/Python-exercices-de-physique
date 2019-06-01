import numpy as np 
import matplotlib.pyplot as plt
coord=[]
temps,donnees=np.loadtxt("C:/Users/pierre/Desktop/pendule.txt",unpack=True)
print(temps,donnees)
def lissage (data,largeur):
    L=[]
    for i in range(len(data)-largeur):
        val=0
        for j in range (largeur):
            val+= data[i+j]
        val/=largeur
        L.append(val)
    return L
largeur=50
donnees_lissees=lissage(donnees,largeur)
temps_lisse =temps[largeur//2:-largeur//2]
plt.plot(temps-temps[0],donnees)
plt.plot(temps_lisse-temps[0],donnees_lissees,linewidth=4)
plt.xlabel("Temps en s")
plt.ylabel("Donnees en V")
plt.show()
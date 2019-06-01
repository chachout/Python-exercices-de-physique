import matplotlib.pyplot as plot 
from pylab import ginput, axis
import numpy as np
T,C = np.loadtxt("pendule.txt",unpack=True)
axis ([5,20,-1,1])
T=np.array([5.808,5.812,5.816,5.82,5.828,5.832,5.836,5.84...])
C=np.array([.....])
print (" là où vous voulez")
point=ginput(1)
print("coordonnées du point cliquer sont")

plot.plot(T,C,'+',color='b')
plot.show()
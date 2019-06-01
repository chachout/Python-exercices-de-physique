import scipy.integrate as integrate
from math import exp


x=[]
y=[]

for z in range(0,50):
    y.append(z/6.07)
    x.append(integrate.simps(59.46*(np.exp(y)-1.0)/(np.exp(y)+1.0)))
import matplotlib.animation as animation
dt=0.0001
fig = figure ()
line, =plot([],[],'bo',ms=10)
xlim(0,2000)
ylim(-1,1)
def animate(i):
    t=i*dt
    xx=x[i]
    y=0.0
    line.set_data(xx,y)
    return line,

ani=animation.FuncAnimation(fig, animate, frames=50, blit=False, interval=100, repeat=False)
show()
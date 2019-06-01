from __future__ import division
from scipy import *
from pylab import *
from scipy.integrate import odeint      # Module de résolution des équations différentielles

R=10000
C=0.001
tau = R*C

def deriv(syst, t):
    q = syst[0]                         # Variable1 N(t)
    dqdt=-q/tau                         # Equation différentielle
    return [dqdt]                       # Dérivées des variables

# Paramètres d'intégration
start = 0
end = 5
numsteps = 50
t = linspace(start,end,numsteps)

# Conditions initiales et résolution
N0=1              
syst_CI=array([N0])                     # Tableau des CI
Sols=odeint(deriv,syst_CI,t)            # Résolution numérique de l'équation différentielle

# Récupération des solutions
N = Sols[:, 0]

# Graphiques des solutions
plot(t, exp(-t), '-b', lw=1.5, label=u"Sol. analytique")          # Solution analytique
plot(t, N, 'o', ms=6, mfc='w', mec='b',label=u"Sol.numérique")  # Solution numérique

xlabel(ur"$t/\tau \, (\varnothing)$", fontsize=16)      # Label de l'axe des abscisses
ylabel(ur"$N/N_{0} \, (\varnothing)$", fontsize=16)     # Label de l'axe des ordonnées

legend()                                                # Appel de la légende
show()
# This script compares the plots of contiguity
# as a function of melt fraction, for 3 different
# formulations.
# Copyright Saswata Hier-Majumder, 2017
from mumap_fwd import *
import matplotlib.pylab as plt

phi1=np.linspace(1.0e-3,0.15)
Basalt=Poroelasticity(phi=phi1)
# The above statement assumes a default dihedral angle of 20.
# To change the dihedral angle to, say, 15,  replace the call above by
# Basalt=Poroelasticity(theta=15.0, phi=phi1)
# Notice that the WHM12 model is insensitive to dihedral angle

plt.figure=1
#Calculate contiguity from von Bargen and Waff, 1986 (default option)
Basalt.set_contiguity()
plt.plot(Basalt.meltfrac,Basalt.Contiguity,'-r')
#Calculate contiguity from Wimert and Hier-Majumder, 2012
Basalt.set_contiguity(contiguity_model=2)
plt.plot(Basalt.meltfrac,Basalt.Contiguity,'-b')
#Calculate contiguity from Hier-Majumder et al. (2006)
Basalt.set_contiguity(contiguity_model=3)
plt.plot(Basalt.meltfrac,Basalt.Contiguity,'-g')
plt.legend(['VBW86','WHM12','HMRB06'])
plt.xlabel('Melt fraction')
plt.ylabel('Contiguity')
plt.show()

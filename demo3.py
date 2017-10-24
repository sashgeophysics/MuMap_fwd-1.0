# This script calculates the reduction in Vp and Vs due
# to melt film inclusions. Three different values
# of melt inclusion aspect ratio are used for comparison
# Copyright Saswata Hier-Majumder, 2017

from mumap_fwd import*
import matplotlib.pylab as plt

#Create an object of class poroelasticity
phi=np.linspace(1.0e-3,0.15)
Basalt=Poroelasticity(phi=phi)
# The above statement assumes a default dihedral angle of 20.
# To change the dihedral angle to, say, X,  replace the call above by
# Basalt=Poroelasticity(theta=X, phi=phi1)
# Notice that the WHM12 model is insensitive to dihedral angle

#Define the highest density of the melt for EOS calculations
Basalt.Melt=Melt(rho=3200.0)
#Calculate the seismic signature for melt films of different aspect ratios
#First plot vs/v0
Basalt.film(aspect=0.1)
plt.plot(Basalt.meltfrac,Basalt.vs_over_v0,'-r')
Basalt.film(aspect=0.01)
plt.plot(Basalt.meltfrac,Basalt.vs_over_v0,'-b')
Basalt.film(aspect=0.001)
plt.plot(Basalt.meltfrac,Basalt.vs_over_v0,'-g')
plt.legend(['0.1','0.01','0.001'],loc=3)
#Vp/v0
Basalt.film(aspect=0.1)
plt.plot(Basalt.meltfrac,Basalt.vp_over_v0,'--r')
Basalt.film(aspect=0.01)
plt.plot(Basalt.meltfrac,Basalt.vp_over_v0,'--b')
Basalt.film(aspect=0.001)
plt.plot(Basalt.meltfrac,Basalt.vp_over_v0,'--g')
plt.xlabel('Melt fraction')
plt.ylabel('V/v0')
plt.title('Vs/V0 and Vp/V0for melt films of different aspect ratios')
plt.show()

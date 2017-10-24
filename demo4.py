# This script calculates shear and P wave speed reduction
# as a function of melt volume fraction for melt tubes with
# a dihedral angle of 20.
# Copyright Saswata Hier-Majumder, 2017


from mumap_fwd import *
import matplotlib.pylab as plt

# Create an object of class poroelasticity
# Define the maximum melt volume fraction as phimax
# Default value of phimax is set to 0.15
phi1=np.linspace(1.0e-3,0.15)
Basalt=Poroelasticity(phi=phi1)
# The above statement assumes a default dihedral angle of 20.
# To change the dihedral angle to, say, 15,  replace the call above by
# Basalt=Poroelasticity(theta=15.0, phi=phi1)
# Notice that the WHM12 model is insensitive to dihedral angle

#Define the highest density of the melt for EOS calculations
Basalt.Melt=Melt(rho=3100.0)
Basalt.Solid=Solid(depth=60.0e3)

Basalt.tube()
plt.figure(1)
plt.plot(Basalt.meltfrac,Basalt.vp_over_v0,'--b')
plt.plot(Basalt.meltfrac,Basalt.vs_over_v0,'--r')
plt.show()
print Basalt.Solid.nu

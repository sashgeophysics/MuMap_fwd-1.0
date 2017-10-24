# This script calculates and compares the reduction in
# Vp and Vs for different melt geometries. This is an example
# of advanced usage of MuMaP_fwd.
# See the annotations below for explanation of the figures.
# Copyright Saswata Hier-Majumder, 2017

from mumap_fwd import *
from matplotlib import rc

plt.rc('text', usetex=True)
# Figure 1 contiguity for different dihedral angles
plt.figure(1)
#Contiguity as function of melt fraction
Rock1=Poroelasticity(theta=5.0,phi=np.linspace(0.0,0.15))
Rock1.set_contiguity()
Rock2=Poroelasticity(theta=40.0,phi=np.linspace(0.0,0.15))
Rock2.set_contiguity()
plt.subplot(2,1,1)
plt.plot(Rock2.meltfrac,Rock2.Contiguity,'-b',linewidth=4)
plt.plot(Rock1.meltfrac,Rock1.Contiguity,'-r', linewidth=4)

plt.fill_between(Rock1.meltfrac,Rock1.Contiguity,Rock2.Contiguity,\
                 color='blue',alpha=0.5)
plt.ylim(0.0,1.0)
# LAbels etc.
plt.rcParams.update({'font.size': 16})
plt.xlabel('Melt volume fraction')
plt.ylabel('Contiguity')
plt.legend([ r"$\theta = 40^{\mathrm{o}}$", r"$\theta = 5^\mathrm{o}$"])
plt.text(0.01,0.2,r'\textbf(a)',fontsize=22)
#Contiguity as function of dihedral angle
Rock1=Poroelasticity(theta=np.linspace(5.0,40.0),phi=0.01)
Rock1.set_contiguity()
Rock2=Poroelasticity(theta=np.linspace(5.0,40.0),phi=0.1)
Rock2.set_contiguity()
plt.subplot(2,1,2)
plt.plot(Rock1.theta,Rock1.Contiguity,'-b', linewidth=4)
plt.plot(Rock2.theta,Rock2.Contiguity,'-r',linewidth=4)
plt.fill_between(Rock1.theta,Rock1.Contiguity,Rock2.Contiguity,\
                 color='green',alpha=0.5)
plt.ylim(0.0,1.0)
# LAbels etc.
plt.rcParams.update({'font.size': 16})
plt.xlabel('Dihedral angle')
plt.ylabel('Contiguity')
plt.legend([ r"$\phi = 0.01$", r"$\phi = 0.1$"],loc=4)
plt.text(7.0,0.8,r'\textbf(b)',fontsize=22)

# Figure 2 Vs/V0 and Vp/V0 for different dihedral angles and melt fractions
plt.figure(2)
#velocity as function of melt fraction
Rock1=Poroelasticity(theta=5.0,phi=np.linspace(1.0e-3,0.1))
Rock1.set_contiguity()
Rock1.tube()
Rock2=Poroelasticity(theta=40.0,phi=np.linspace(1.0e-3,0.1))
Rock2.set_contiguity()
Rock2.tube()
plt.subplot(2,1,1)
plt.plot(Rock2.meltfrac,Rock2.vs_over_v0,'-b',linewidth=4)
plt.plot(Rock1.meltfrac,Rock1.vs_over_v0,'-r', linewidth=4)
#plt.fill_between(Rock1.meltfrac,Rock1.vs_over_v0,Rock2.vs_over_v0,\
#                 color='blue',alpha=0.5)
plt.plot(Rock2.meltfrac,Rock2.vp_over_v0,'--b',linewidth=4)
plt.plot(Rock1.meltfrac,Rock1.vp_over_v0,'--r', linewidth=4)
#plt.fill_between(Rock1.meltfrac,Rock1.vp_over_v0,Rock2.vp_over_v0,\
#                 color='red',alpha=0.5)

plt.ylim(0.5,1.0)
plt.xlim(0.0,0.1)
# Labels etc.
plt.rcParams.update({'font.size': 16})
plt.xlabel('Melt volume fraction')
plt.ylabel(r'$V/V_0$')
plt.legend([ r"$\theta = 40^{\mathrm{o}}$", r"$\theta = 5^\mathrm{o}$"],loc=3)
plt.text(0.005,0.9,r'\textbf(a)',fontsize=22)
plt.plot(np.linspace(0.04,0.045,10),np.zeros(10)+0.65,'--b',linewidth=4)
plt.plot(np.linspace(0.04,0.045,10),np.zeros(10)+0.63,'--r',linewidth=4)
plt.plot(np.linspace(0.04,0.045,10),np.zeros(10)+0.59,'-b',linewidth=4)
plt.plot(np.linspace(0.04,0.045,10),np.zeros(10)+0.57,'-r',linewidth=4)
plt.text(0.048,0.63,r'$V_P/V_0$')
plt.text(0.048,0.56,r'$V_S/V_0$')
#V/V0 as function of dihedral angle
Rock1=Poroelasticity(theta=np.linspace(5.0,40.0),phi=0.01)
Rock1.set_contiguity()
Rock1.tube()
Rock2=Poroelasticity(theta=np.linspace(5.0,40.0),phi=0.1)
Rock2.set_contiguity()
Rock2.tube()
plt.subplot(2,1,2)
plt.plot(Rock1.theta,Rock1.vs_over_v0,'-b', linewidth=4)
plt.plot(Rock2.theta,Rock2.vs_over_v0,'-r',linewidth=4)
#plt.fill_between(Rock1.theta,Rock1.vs_over_v0,Rock2.vs_over_v0,\
#                 color='blue',alpha=0.5)
plt.plot(Rock1.theta,Rock1.vp_over_v0,'--b', linewidth=4)
plt.plot(Rock2.theta,Rock2.vp_over_v0,'--r',linewidth=4)
#plt.fill_between(Rock1.theta,Rock1.vp_over_v0,Rock2.vp_over_v0,\
#                 color='red',alpha=0.5)
plt.ylim(0.5,1.0)
# LAbels etc.
plt.rcParams.update({'font.size': 16})
plt.xlabel('Dihedral angle')
plt.ylabel(r'$V/V_0$')
plt.legend([ r"$\phi = 0.01$", r"$\phi = 0.1$"],loc=4)
plt.text(7.0,0.9,r'\textbf(b)',fontsize=22)

plt.plot(np.linspace(15.0,18.0,10),np.zeros(10)+0.65,'--b',linewidth=4)
plt.plot(np.linspace(15.0,18.0,10),np.zeros(10)+0.63,'--r',linewidth=4)

plt.plot(np.linspace(15.0,18.0,10),np.zeros(10)+0.59,'-b',linewidth=4)
plt.plot(np.linspace(15.0,18.0,10),np.zeros(10)+0.57,'-r',linewidth=4)

plt.text(19.0,0.63,r'$V_P/V_0$')
plt.text(19.0,0.56,r'$V_S/V_0$')

# Plot comparing vs and vp reduction due to melting for tubes and pockets

plt.figure(3)
Rock2=Poroelasticity(theta=5.0,phi=np.linspace(1.0e-3,0.1))
Rock2.film(aspect=0.1)
plt.plot(Rock2.meltfrac,Rock2.vp_over_v0,'-.b', linewidth=4)
plt.plot(Rock2.meltfrac,Rock2.vs_over_v0,'-.r', linewidth=4)

Rock1=Poroelasticity(theta=20.0,phi=np.linspace(1.0e-3,0.1))
Rock1.set_contiguity()
Rock1.tube()
plt.plot(Rock1.meltfrac,Rock1.vp_over_v0,'-b', linewidth=4)
plt.plot(Rock1.meltfrac,Rock1.vs_over_v0,'-r', linewidth=4)

Rock2.film(aspect=0.01)
plt.plot(Rock2.meltfrac,Rock2.vp_over_v0,'--b', linewidth=4)
plt.plot(Rock2.meltfrac,Rock2.vs_over_v0,'--r', linewidth=4)

#Lables
plt.rcParams.update({'font.size': 16})
plt.xlabel('Melt fraction')
plt.ylabel(r"$V/V_0$")
plt.legend([r"$V_P/V_0$, film (0.1)", r"$V_S/V_0$, film (0.1)", r"$V_P/V_0$, tube $(20^\mathrm{o})$", r"$V_S/V_0$, tube ($20^\mathrm{o}$)",r"$V_P/V_0$, film (0.01)", r"$V_S/V_0$, film (0.01)"],loc=3)
plt.xlim(0.0,0.1)


plt.show()

# After showing the figure, print out the relevant information on
# command prompt
print '================================================================='
print 'Bulk and shear Moduli of solid (GPa:)', Rock1.Solid.K/1.0e9\
    ,Rock1.Solid.G/1.0e9
print 'Bulk Modulus of Melt (GPa):', np.max(Rock1.Melt.Melt_EOS.K)/1.0e9
print 'Density of solid and melt (kg/m^3):', Rock1.Solid.rho,\
    np.max(Rock1.Melt.Melt_EOS.rho)
print '================================================================='

## Calculate some characteristic values
## For melt tubes
Rock1=Poroelasticity(theta=5.0,phi=0.01)
Rock1.set_contiguity()
Rock1.tube()
Rock2=Poroelasticity(theta=40.0,phi=0.01)
Rock2.set_contiguity()
Rock2.tube()

print'==================================================================='
print 'For a dihedral angle and melt fraction of', Rock1.theta, Rock1.meltfrac
print 'Vs/V0 and VP/V0 are:',Rock1.vs_over_v0, Rock1.vp_over_v0
print'==================================================================='
print 'For a dihedral angle and melt fraction of', Rock2.theta, Rock2.meltfrac
print 'Vs/V0 and VP/V0 are:',Rock2.vs_over_v0, Rock2.vp_over_v0
print'==================================================================='

#calculate some characteristic values for melt films
Rock1=Poroelasticity(theta=20.0,phi=0.01)
Rock1.set_contiguity()
Rock1.tube()
Rock2=Poroelasticity(theta=20.0,phi=0.01)
Rock2.film(aspect=0.1)
Rock3=Poroelasticity(theta=20.0,phi=0.01)
Rock3.film(aspect=0.01)
print'==================================================================='
print 'For a dihedral angle and melt fraction of', Rock1.theta, Rock1.meltfrac
print 'Vs/V0 and VP/V0 are:',Rock1.vs_over_v0, Rock1.vp_over_v0
print'==================================================================='
print 'For a film aspect ratio and melt fraction of', Rock2.aspect, Rock2.meltfrac
print 'Vs/V0 and VP/V0 are:',Rock2.vs_over_v0, Rock2.vp_over_v0
print'==================================================================='
print'==================================================================='
print 'For a film aspect ratio and melt fraction of', Rock3.aspect, Rock3.meltfrac
print 'Vs/V0 and VP/V0 are:',Rock3.vs_over_v0, Rock3.vp_over_v0
print'==================================================================='

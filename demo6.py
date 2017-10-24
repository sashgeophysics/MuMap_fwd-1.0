from mumap_fwd import *
from matplotlib import rc

# Read the data from file
# The column contents are, from left to right
# Pressure (GPa), Depth (km), Temperature (K),Density (g/cm^3),\
#    Basalt fraction, Vs(km/s), Vp(km/s), Entropy(J/g.K)

dat1000=np.genfromtxt('LAB1000X04.dat')
dat1200=np.genfromtxt('LAB1200X04.dat')
depth=dat1000[:,1]*1.0e3
[G1000,K1000,nu1000]=Velocity_to_Moduli(dat1000[:,5]*1.0e3,\
                                        dat1000[:,6]*1.0e3,dat1000[:,3]*1.0e3)
[G1200,K1200,nu1200]=Velocity_to_Moduli(dat1200[:,5]*1.0e3,\
                                        dat1200[:,6]*1.0e3,dat1200[:,3]*1.0e3)

# Insert a partially molten region between 60 and 80 km depth
phi=0.0*depth+1.0e-4 # Create an array with zero melt fraction
ind=np.where((depth >= 60.0e3) & (depth < 80.0e3))
phi[ind]=0.01

#Create an object containing the melt fraction array
Rock1=Poroelasticity(theta=20.0,phi=phi)
Rock2=Poroelasticity(phi=phi)
#Assign the solid physical properties from the data
Rock1.Solid.K=K1000
Rock1.Solid.G=G1000
Rock1.Solid.rho=dat1000[:,3]*1.0e3
Rock1.Solid.Depth=depth
Rock1.Solid.nu=nu1000
# Calculate contiguity
Rock1.Melt.Melt_EOS.Vinet()
Rock2.Solid=Rock1.Solid
Rock2.Melt=Rock1.Melt
Rock1.set_contiguity()
Rock1.tube()

Rock2.film(aspect=0.01)
# Make the plots
plt.rc('text', usetex=True)
plt.figure(1)
# Plot the Vs profile
plt.plot(Rock2.vs_over_v0*dat1000[:,5],dat1000[:,1],'-g',linewidth=4)
plt.plot(Rock1.vs_over_v0*dat1000[:,5],dat1000[:,1],'-k',linewidth=4)
plt.legend([r'Film ($\alpha$=0.01)',r"Tube $\theta = 20^\mathrm{o}$"],loc=4)
plt.plot(dat1200[:,5],dat1200[:,1],'-r',linewidth=4)
plt.plot(dat1000[:,5],dat1000[:,1],'-b',linewidth=4)



# Plot the Vp profile
plt.plot(Rock2.vp_over_v0*dat1000[:,6],dat1000[:,1],'-g',linewidth=4)
plt.plot(Rock1.vp_over_v0*dat1000[:,6],dat1000[:,1],'-k',linewidth=4)
plt.plot(dat1000[:,6],dat1000[:,1],'--b',linewidth=4)
plt.plot(dat1200[:,6],dat1200[:,1],'--r',linewidth=4)

plt.ylim(160.0,0.0)

# Labels
#plt.legend(['Shear (1000 K)', 'Shear (1200K)', \
#            'Bulk (1000 K)', 'Bulk(1200 K)'], loc=3)
plt.rcParams.update({'font.size': 16})
plt.xlabel('Wave speed (km/s)')
plt.ylabel('Depth (km)')

plt.figure(2)
# Plot the Shear modulus profile
plt.plot(G1000/1.0e9,depth/1.0e3,'-b',linewidth=4)
plt.plot(G1200/1.0e9,depth/1.0e3,'-r',linewidth=4)

# Plot the Bulk modulus profile
plt.plot(K1000/1.0e9,depth/1.0e3,'--b',linewidth=4)
plt.plot(K1200/1.0e9,depth/1.0e3,'--r',linewidth=4)

# Labels
#plt.legend(['Shear (1000 K)', 'Shear (1200K)', \
#            'Bulk (1000 K)', 'Bulk(1200 K)'], loc=3)
plt.rcParams.update({'font.size': 16})
plt.xlabel('Elastic moduli (GPa)')
plt.ylabel('Depth (km)')

plt.ylim(160.0,0.0)


plt.show()


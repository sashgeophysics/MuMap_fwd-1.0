# This script plots the density of various silicic
# melts as a function of pressure. 
# See the docstring under class melt for details
# The default high density for the melts is 4000 kg/m3
# To set the density to a higher or lower value,
# set the variable rho_high to the desired value
# while instantiating the object
# The default melt composition is
# Peridotite melt of Guillot and Sator (2007)
# To select other available melt compositions set
# the parameter melt_comp to different values.
# Copyright Saswata Hier-Majumder, 2017

from mumap_fwd import *
import matplotlib.pylab as plt


# Create an array of melt density
rho1=np.linspace(2800.0,4000.0)
# Initiate melts of different composition.
Peridotite_GS07=Melt(rho=rho1)
MORB_GS07=Melt(melt_comp=2,rho=rho1)
Peridotite_OM01=Melt(melt_comp=3,rho=rho1)
MORB_OM01=Melt(melt_comp=4,rho=rho1)
Peridotite_CO2=Melt(melt_comp=5,rho=rho1)


# Calculate pressure for the melts using the Vinet EOS
# To use the third order Birch-Murnaghan EOS, replace Melt_EOS.Vinet()
# in the following calls by Melt_EOS.BM3()

Peridotite_GS07.Melt_EOS.Vinet()

MORB_GS07.Melt_EOS.Vinet()

Peridotite_OM01.Melt_EOS.Vinet()

MORB_OM01.Melt_EOS.Vinet()

Peridotite_CO2.Melt_EOS.Vinet()

# Peridotite_GS07.Melt_EOS.BM3()
# MORB_GS07.Melt_EOS.BM3()
# Peridotite_OM01.Melt_EOS.BM3()
# MORB_OM01.Melt_EOS.BM3()
# Peridotite_CO2.Melt_EOS.BM3()

#Plot pressure (in GPa) vs density for peridotite melts
plt.figure(1)
plt.plot(Peridotite_GS07.Melt_EOS.P/1.0e9,Peridotite_GS07.Melt_EOS.rho,'-r')
plt.plot(Peridotite_OM01.Melt_EOS.P/1.0e9,Peridotite_OM01.Melt_EOS.rho,'-b')
plt.plot(Peridotite_CO2.Melt_EOS.P/1.0e9,Peridotite_CO2.Melt_EOS.rho,'-g')
plt.legend(['GS07','OM01','Ghosh07 CO2'],loc=4)
plt.xlabel('Pressure (GPa)')
plt.ylabel('Density (kg/m3)')
plt.title('Peridotite melt EOS')

#plot pressure (in GPa) vs density for MORB
plt.figure(2)
plt.plot(MORB_GS07.Melt_EOS.P/1.0e9,MORB_GS07.Melt_EOS.rho,'-r')
plt.plot(MORB_OM01.Melt_EOS.P/1.0e9,MORB_OM01.Melt_EOS.rho,'-b')
plt.legend(['GS07','OM01'],loc=4)
plt.xlabel('Pressure (GPa)')
plt.ylabel('Density (kg/m3)')
plt.title('MORB EOS')
plt.show()

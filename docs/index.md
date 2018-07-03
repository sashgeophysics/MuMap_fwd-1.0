
# MuMaP_fwd
## Copyright Saswata Hier-Majumder, 2017
## Royal Holloway University of London  

This module contains classes and functions relevant to calculate the
effect of melting on the elastic moduli and seismic wave velocities in 
partially molten rocks. To run the demonstrations, a working version of
Python 2.7.12 or higher, numpy, and matplotlib libraries are required.  

See the [Wiki pages](https://github.com/sashgeophysics/MuMap_fwd/wiki)  for detailed documentation. Scroll down for a quick start guide

## Quick start guide
* Download the files from GitHub as a zipped file
* Extract the files
* Open a terminal or your preferred mode of running python and type in  
>python demo1.py  

This should execute the file and create a plot.  

Go to the Project wiki pages and work through the tutorials. Each tutorial is associated with a demo file. The in-line documentation within the source files is explained in detail in the wiki file. You can also cut and paste the following code snippets into your python terminal to get a quick sample of MuMaP_fwd.  
### Example1:   
Plot Vinet equation of state of MORB using parameters  
from Guillot and Sator(2007), run demo2.py for more plots  

>     from mumap_fwd import *  
>     import matplotlib.pylab as plt  
>     rho1=np.linspace(2800.0,4000.0)  
>     melt1=Melt(melt_comp=2,rho=rho1)  
>     melt1.Melt_EOS.Vinet()  
>     plt.plot(melt1.Melt_EOS.P/1.0e9,melt1.Melt_EOS.rho)  
>     plt.show()  

### Example 2:  
Plot the Vs/V0 as a function of melt fraction. In this case  
all the melt resides in films of aspect ratio 0.01. This uses the formulation  
of Walsh, 1969   

>     from mumap_fwd import*  
>     import matplotlib.pylab as plt  
>     phi=np.linspace(1.0e-3,0.15)  
>     rock=Poroelasticity(phi=phi)  
>     rock.Melt=Melt(rho=3200.0)  
>     rock.film(aspect=0.01)  
>     plt.plot(rock.meltfrac,rock.vs_over_v0)  
>     plt.show()  

### Example 3:
Plot Vs/V0 as a function of melt fraction. In this case, the melt geometry  
is calculated from von Bargen and Waff (1986) and the effective elastic  
moduli are calculated following Hier-Majumder et al. (2014). Run demo4.py  
for more information.     

>     from mumap_fwd import *
>     import matplotlib.pylab as plt
>     phi1=np.linspace(1.0e-3,0.15)
>     rock=Poroelasticity(phi=phi1)
>     rock.tube()
>     plt.plot(rock.meltfrac,rock.vs_over_v0)  
>     plt.show() 

Use the tutorials to try out the different features of MuMap_fwd. The tutorial progress in order of difficulty. The files corresponding to tutorials are named as demox.py, where x is the tutorial number
## To cite MuMap_fwd:  

Please cite these following papers which contain much of the material involved in MuMaP_fwd. Please also see the list of references for a full list of articles or databases used in writing this code.  

* Saswata Hier-Majumder. (2017, November 2). MuMap_fwd-1.0 (Version 1.0). Zenodo. [http://doi.org/10.5281/zenodo.1040971](http://doi.org/10.5281/zenodo.1040971)
* Hier-Majumder, S., Keel, E. B., & Courtier, A. M. (2014). The influence of temperature, bulk composition, and melting on the seismic signature of the low-velocity layer above the transition zone. Journal of Geophysical Research: Solid Earth, 119(2), 971–983. [https://doi.org/10.1002/2013JB010314](https://doi.org/10.1002/2013JB010314)
* Hier-Majumder, S. (2008). Influence of contiguity on seismic velocities of partially molten aggregates. Journal of Geophysical Research, 113(B12), B12205. [https://doi.org/10.1029/2008JB005662](https://doi.org/10.1029/2008JB005662)  

## Brief description  

Detailed description for each class is provided in the wiki pages.

[EOS](https://github.com/sashgeophysics/MuMap_fwd/wiki/Class-EOS): Contains functions for equations of state for solids and melts.
This class also contains the PREM model of Dziewonski and Anderson (1984). 
To initiate this class for a given material known values of some paramters 
need to be provided. In most cases, this class will be initiated from
either the Solid or the Melt class, which contain default values for the 
parameters.  

[Solid](https://github.com/sashgeophysics/MuMap_fwd/wiki/Class-Solid): This class contains a number of variables and functions relating
to the properties of the solid. All of the parameters are provided with
a default value. See the docstring for more details. By default, this class 
uses the PREM model to evaluate the elastic properties corresponding to the
depth parameter provided during instantiation.  

[Melt](https://github.com/sashgeophysics/MuMap_fwd/wiki/Class-Melt): This class contains physical paramters for calculating the EOS of the
melt. It also defaults to a dihedral angle of 15 degrees. The choice
of parameters for the EOS are set by the variable melt_comp. Please
see the docstring for __init__ for a full description of the currently
available choices.  

[Poroelasticity](https://github.com/sashgeophysics/MuMap_fwd/wiki/Class-Poroelasticity):  This class contains functions for calculating effective
elastic properties for a given melt fraction and physical properties
of the solid and the melt, contained in those classes. This class contains
three choices of contiguity models, see the docstrings for more information.
The default model is von Bargen and Waff, which allows for variation
in the dihedral angle. Do not use this model for higher melt fractions.   


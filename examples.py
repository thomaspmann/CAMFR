from __future__ import division
from camfr import *
from RCLED import *


def edts():
    set_lambda(1.55)
    set_N(20)
    set_polarisation(TE)

    # Define waveguide.
    slab = Slab(SiO2(2) + EDTS(1.5) + air(2))
    slab.calc()

    # Print out some waveguide characteristics.
    print slab.mode(0).kz()
    print slab.mode(0).n_eff()

    # Do some interactive plotting.
    r_x = arange(0, slab.width(), 0.1)
    slab.plot_n(r_x)
    slab.plot()


def dipole_emission():
    # Set parameters.
    set_lambda(1.55)

    # Create materials.
    SiO2 = Material(1.45)
    EDTS = Material(1.6)
    absorbing = Material(1.45-0.5j)
    air = Material(1.0)

    # Define layer structure.
    top = Uniform(EDTS, 0.1) + \
          Uniform(absorbing, 2) + \
          Uniform(air, 0.000)

    bot = Uniform(EDTS, 1.0) + \
          Uniform(SiO2, 0.000)

    sub = Uniform(SiO2, 0.000) + \
          Uniform(air, 0.000)

    ref = Uniform(10)

    cav = RCLED(top, bot, sub, ref)

    # Calculate.
    cav.calc()
    # Plot
    cav.radiation_profile(horizontal)


if __name__ == "__main__":

    # Define materials refractive index.
    SiO2 = Material(1.45)
    EDTS = Material(1.6)
    air = Material(1.0)

    # edts()
    dipole_emission()
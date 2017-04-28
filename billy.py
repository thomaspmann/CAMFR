from __future__ import division
from camfr import *


def circular():
    """Cylinder/disk Waveguide"""
    set_lambda(1.55)
    set_N(20)
    set_circ_order(0)
    # set_polarisation(TM)  # Bessel order = 0 above therefore not used in the calculation
    set_circ_PML(-0.1)

    # Define uniform circular waveguide.
    r = 58.91/2   # Radius of the disk
    d = 1.5  # Thickness of the waveguide
    p = 2.0  # cladding padding
    wg = Circ(EDTS(r) + air(p))

    wg.calc()
    te01 = 0
    # print("Disk modes:")
    for i in arange(0, N(), 1):
        # print(wg.mode(i).n_eff())
        # Find TE01 mode as having n_eff closest to 1.
        if abs(1 - wg.mode(i).n_eff().real) < abs(1 - wg.mode(te01).n_eff().real):
            te01 = i
    print("\nTE01 Mode n_eff {:.3} and kz {:.3}".format(wg.mode(te01).n_eff(), wg.mode(te01).kz()))

    # superstrate = Circ(air(r+p))
    # substrate = Circ(SiO2(r+p))
    # stack = Stack(substrate(0.0) + wg(d) + superstrate(0.0))
    #
    # stack.calc()
    # print(r, abs(stack.R12(0, 0)))
    # print(wg.mode(te01).kz())
    # print(wg.mode(te01).n_eff())
    # free_tmps()


def ring():
    """Ring Waveguide"""
    set_lambda(1.55)
    set_N(40)
    set_circ_order(0)
    # set_polarisation(TM)  # Bessel order = 0 above therefore not used in the calculation
    set_circ_PML(-0.1)

    # Define uniform ring waveguide.
    r_in = 83.81/2  # Radius of the inner waveguide ring
    r_out = 100.54/2  # Radius of the outer waveguide ring
    r_d = r_out - r_in  # Diameter of the ring
    d = 1.5  # Thickness of the waveguide
    p = 2.0  # cladding padding
    wg = Circ(air(r_in) + EDTS(r_d) + air(p))
    # wg.plot_n(arange(0, r_in+r_d+p, 0.1))
    wg.calc()
    te01 = 0
    # print("Disk modes:")
    for i in arange(0, N(), 1):
        # print(wg.mode(i).n_eff())
        # Find TE01 mode as having n_eff closest to 1.
        if abs(1 - wg.mode(i).n_eff().real) < abs(1 - wg.mode(te01).n_eff().real):
            te01 = i
    print("\nTE01 Mode n_eff {:.3} and kz {:.3}".format(wg.mode(te01).n_eff(), wg.mode(te01).kz()))

    superstrate = Circ(air(r_in+r_d+p))
    substrate = Circ(SiO2(r_in+r_d+p))
    stack = Stack(substrate(0) + wg(d) + superstrate(0))
    # Calculate
    stack.calc()
    print(stack.mode(te01).kz())


if __name__ == "__main__":

    # Define materials refractive index.
    SiO2 = Material(1.45)
    EDTS = Material(1.6)
    air = Material(1.0)

    print('Disk Waveguide:')
    circular()
    print('Ring Waveguide:')
    ring()

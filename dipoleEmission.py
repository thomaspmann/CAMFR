"""
Code to simulate the emission of a dipole as a function of position within multilayer structures.

Note emission rates are normalised to the free space emission rate by multiplying power by layer n.
"""

from __future__ import division, print_function
# from camfr import *
from RCLED import *
import numpy as np
from tqdm import tqdm


def example1():
    """Dipole emission in a semi-infinite Si-air layered structure."""

    # Set parameters.
    lam0 = 1.55
    set_lambda(lam0)

    # Create materials.
    Si = Material(3.48)
    air = Material(1.0)

    d_list = np.linspace(-lam0, lam0, 300)

    h = []
    v = []
    for d in tqdm(d_list):
        if d <= 0:  # In Si layer
            # Define layer structure.
            top = Uniform(Si, -d) + \
                  Uniform(air, 0.0)

            bot = Uniform(Si, 0.0)

            sub = Uniform(Si, 0.0)

            n_layer = Si.n()

        else:  # In air layer
            # Define layer structure.
            top = Uniform(air, 0.0)

            bot = Uniform(air, d) + \
                  Uniform(Si, 0.0)

            sub = Uniform(Si, 0.0)
            n_layer = air.n()

        ref = Uniform(10)
        cav = RCLED(top, bot, sub, ref)
        res = cav.calc()
        h.append(res[horizontal].P_source * n_layer)
        v.append(res[vertical].P_source * n_layer)

        del cav

    fig, ax = plt.subplots()
    ax.plot(d_list, h, label='h')
    ax.plot(d_list, v, label='v')
    ax.set_ylabel('$\Gamma /\Gamma_0$')
    ax.set_xlabel('z/$\lambda$')
    plt.legend()
    plt.show()


def example2():
    """Dipole emission in an EDTS film bounded by SiO2/Air (substrate) air (superstrate)."""

    # Set parameters.
    lam0 = 1.55
    set_lambda(lam0)

    # Create materials.
    SiO2 = Material(1.42)
    EDTS = Material(1.6)
    air = Material(1.0)
    water = Material(1.3180-0.000098625j)
    d20 = Material(1.3170-0.0000044651j)

    d_list = np.linspace(0, 1.4, 100)

    h = []
    v = []
    avg = []
    for d in tqdm(d_list):
        # Define layer structure.
        top = Uniform(EDTS, 1.4-d) + \
              Uniform(d20, 0.0)

        bot = Uniform(EDTS, d) + \
              Uniform(SiO2, 0.0)

        sub = Uniform(SiO2, 0.0) + \
              Uniform(air, 0.0)

        n_layer = EDTS.n()
        ref = Uniform(10)
        cav = RCLED(top, bot, sub, ref)
        res = cav.calc()
        h.append(res[horizontal].P_source * n_layer.real)
        v.append(res[vertical].P_source * n_layer.real)
        avg.append(res.P_source * n_layer)

        del cav

    fig, ax = plt.subplots()
    # ax.plot(d_list, h, label='h')
    # ax.plot(d_list, v, label='v')
    ax.plot(d_list, avg, label='avg')
    ax.set_ylabel('$\Gamma /\Gamma_0$')
    ax.set_xlabel('z/$\lambda$')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # example1()
    example2()

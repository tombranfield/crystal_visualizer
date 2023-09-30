"""bond_calculations.py

This module contains functions for the calculation of bond lengths and bond
angles.
"""

import numpy as np

from crystal_visualizer.atom import Atom
from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.metric_tensor import metric_tensor


def bond_length(
    atom_1: Atom, 
    atom_2: Atom, 
    lattice_parameters: LatticeParameters
) -> float:
    """Calculates the length of a bond between two atoms in Angstroms"""
    r1 = atom_1.position()
    r2 = atom_2.position()
    r = r2 - r1
    g = metric_tensor(lattice_parameters)
    bond_length = np.sqrt(r @ (g @ r))
    return bond_length


def bond_angle(
    atom_1: Atom,
    atom_2: Atom,
    atom_3: Atom,
    lattice_parameters: LatticeParameters
) -> float:
    """
    Calculates the bond angle between 3 atoms. Returns the result in degrees.

    atom_1 is bonded to atom_2. atom_3 is also bonded to atom_2. This function
    calculates the angle between the vector connecting atom_1 to atom_2, and
    the vector connecting atom_3 to atom_2.
    """
    r1 = atom_1.position()
    r2 = atom_2.position()
    r3 = atom_3.position()
    s = r1 - r2
    t = r3 - r2
    g = metric_tensor(lattice_parameters)

    # Calculating an intermediate matrix that contains 3 necessary dot products
    # See pg.85 "Structure of Materials for more info
    # This matrix only used for bond angle, hence inside bond angle function
    m = np.array([s, t]) @ (g @ np.transpose(np.array([s, t])))

    s_dot_t = m[0, 1]
    s_dot_s = m[0, 0]
    t_dot_t = m[1, 1]

    bond_angle = np.arccos(s_dot_t / np.sqrt(s_dot_s * t_dot_t))
    return np.rad2deg(bond_angle)








if __name__ == "__main__":
    lp = LatticeParameters(1, 1, 1, 90, 90, 90)
    atom_1 = Atom("Ti", 1/2, 1/2, 0.0)
    atom_2 = Atom("O", 0.0, 0.0, 0.0)
    atom_3 = Atom("Ti", 1/2, 0.0, 1/2)
    angle = bond_angle(atom_1, atom_2, atom_3, lp)
    print(angle, "deg")

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
    bond_length = np.sqrt(r @ g @ r)
    return bond_length


if __name__ == "__main__":
    atom_1 = Atom("Fe", 1/2, 1/3, 1/4)
    atom_2 = Atom("O", 1/3, 1/2, 3/4)
    lattice_parameters = LatticeParameters(2, 2, 3, 90, 90, 90)
    bond_length = bond_length(atom_1, atom_2, lattice_parameters)
    print(bond_length)

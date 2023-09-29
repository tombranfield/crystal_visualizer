"""bond_calculations.py

This module contains functions for the calculation of bond lengths and bond
angles.
"""

from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.metric_tensor import metric_tensor


def bond_length(
    atom_1: Atom, 
    atom_2: Atom, 
    lattice_parameters: LatticeParameters
) -> float:
    """Calculates the length of a bond between two atoms in Angstroms"""
    r1 = atom_1.position
    r2 = atom_2.position
    r = r2 - r1
    g = metric_tensor(lattice_parameters)
    bond_length = np.sqrt(r @ g @ r)
    return bond_length

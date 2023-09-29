"""test_bond_calculations.py"""

import numpy as np

from crystal_visualizer.atom import Atom
from crystal_visualizer.bond_calculations import bond_length
from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.metric_tensor import metric_tensor


# Checking result vs the example pg.83 of "Structure of Materials"
def test_bond_length_1():
    atom_1 = Atom("Fe", 1/2, 1/3, 1/4)
    atom_2 = Atom("O", 1/3, 1/2, 3/4)
    lattice_parameters = LatticeParameters(2, 2, 3, 90, 90, 90)
    _bond_length = bond_length(atom_1, atom_2, lattice_parameters)
    bond_length_3dp = float(str(_bond_length)[:5])
    assert bond_length_3dp == 1.572    

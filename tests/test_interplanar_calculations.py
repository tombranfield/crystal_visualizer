"""test_interplanar_calculations.py"""

import numpy as np

from crystal_visualizer.hkl import HKL
from crystal_visualizer.interplanar_calculations import interplanar_distance
from crystal_visualizer.lattice_parameters import LatticeParameters


# From example (i) on pg.114 of "Structure of Materials"
def test_interplanar_spacing_successfully_calculated_for_cubic():
    lp = LatticeParameters(2, 2, 2, 90, 90, 90)
    plane_hkl = HKL(1, 1, 0)
    calculated_spacing = interplanar_distance(plane_hkl, lp)
    calculated_3dp = float(str(calculated_spacing)[:5])
    expected_spacing = 1.414
    assert calculated_3dp == expected_spacing

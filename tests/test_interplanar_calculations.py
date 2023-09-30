"""test_interplanar_calculations.py"""

import numpy as np

from crystal_visualizer.hkl import HKL
from crystal_visualizer.interplanar_calculations import interplanar_distance, interplanar_angle
from crystal_visualizer.lattice_parameters import LatticeParameters


# From example (i) on pg.114 of "Structure of Materials"
def test_interplanar_spacing_successfully_calculated_for_cubic():
    lp = LatticeParameters(2, 2, 2, 90, 90, 90)
    plane_hkl = HKL(1, 1, 0)
    calculated_spacing = interplanar_distance(plane_hkl, lp)
    calculated_spacing_3dp = float(str(calculated_spacing)[:5])
    expected_spacing = 1.414
    assert calculated_spacing_3dp == expected_spacing


def test_interplanar_angle():
    lp = LatticeParameters(4, 6, 5, 90, 120, 90)
    hkl_1 = HKL(1, 0, 1)
    hkl_2 = HKL(-2, 0, 1)
    calculated_angle = interplanar_angle(hkl_1, hkl_2, lp)
    calculated_angle_3dp = float(str(calculated_angle)[:6])
    expected_angle = 130.25
    assert calculated_angle_3dp == expected_angle

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


# From example (ii) pg.115 of "Structure of Materials"
def test_interplanar_spacing_successfully_calculated_for_monoclinic():
    lp = LatticeParameters(3, 4, 6, 90, 90, 120)
    plane_hkl = HKL(1, 1, 1)
    calculated_spacing = interplanar_distance(plane_hkl, lp)
    calculated_spacing_3dp = float(str(calculated_spacing)[:5])
    expected_spacing = 1.643
    assert calculated_spacing_3dp == expected_spacing


# From example (iii) pg.117 of "Structure of Materials"
def test_interplanar_angle_calculated_correctly():
    lp = LatticeParameters(4, 6, 5, 90, 120, 90)
    hkl_1 = HKL(1, 0, 1)
    hkl_2 = HKL(-2, 0, 1)
    calculated_angle = interplanar_angle(hkl_1, hkl_2, lp)
    calculated_angle_3dp = float(str(calculated_angle)[:6])
    expected_angle = 130.25
    assert calculated_angle_3dp == expected_angle


# From selected problems pg.120 of "Structure of Materials"
def test_interplanar_distances_of_goethite_calculated_correctly():
    lp = LatticeParameters(0.4596, 0.9957, 0.3021, 90, 90, 90)
    plane_1 = HKL(0,2,0)
    plane_2 = HKL(2,0,0)
    plane_3 = HKL(1,1,1)
    calculated_spacing_1 = round(interplanar_distance(plane_1, lp), 3)
    calculated_spacing_2 = round(interplanar_distance(plane_2, lp), 3)
    calculated_spacing_3 = round(interplanar_distance(plane_3, lp), 3)
    expected_spacing_1 = 0.498
    expected_spacing_2 = 0.230
    expected_spacing_3 = 0.245
    assert calculated_spacing_1 == expected_spacing_1
    assert calculated_spacing_2 == expected_spacing_2
    assert calculated_spacing_3 == expected_spacing_3
    

def test_interplanar_angle_of_goethite_calculated_correctly():
    lp = LatticeParameters(0.4596, 0.9957, 0.3021, 90, 90, 90)
    plane_1 = HKL(1, 0, 1)
    plane_2 = HKL(-1, 0, 1)
    calculated_angle = round(interplanar_angle(plane_1, plane_2, lp), 1)
    expected_angle = 66.6
    assert calculated_angle == expected_angle

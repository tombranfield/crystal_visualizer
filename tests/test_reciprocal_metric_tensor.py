"""test_reciprocal_metric_tensor.py"""

import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.reciprocal_metric_tensor import reciprocal_metric_tensor
from crystal_visualizer.reciprocal_metric_tensor import volume



def test_volume_of_cube_calculated_correctly_direct_space():
    lp = LatticeParameters(10, 10, 10, 90, 90, 90)
    calculated_volume = volume(lp)
    expected_volume = 1000
    assert calculated_volume == expected_volume


def test_volume_of_tetrahedron_calculated_correctly_direct_space():
    lp = LatticeParameters(2, 3, 4, 90, 90, 90)
    calculated_volume = volume(lp)
    expected_volume = 24
    assert expected_volume == expected_volume


def test_volume_of_triclinic_lattice_correctly_direct_space():
    lp = LatticeParameters(3, 4, 6, 90, 90, 120)
    calculated_volume = volume(lp)
    expected_volume = np.sqrt(3888)
    assert np.allclose(calculated_volume, expected_volume)

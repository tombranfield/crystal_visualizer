"""test_metric_tensor.py"""


import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.metric_tensor import metric_tensor


def test_metric_tensor_for_cubic_lattice():
    lp = LatticeParameters(1, 1, 1, 90, 90, 90)
    g = metric_tensor(lp)
    expected = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert np.allclose(g, expected)

def test_metric_tensor_for_hexagonal_lattice():
    lp = LatticeParameters(1, 1, 2, 90, 90, 120)
    g = metric_tensor(lp)
    expected = np.array([[1, -1/2, 0], [-1/2, 1, 0], [0, 0, 4]])
    assert np.allclose(g, expected)

def test_metric_tensor_for_monoclinic_lattice():
    lp = LatticeParameters(1, 2, 3, 90, 135, 90)
    g = metric_tensor(lp)
    expected = ([
        [1, 0, 3*np.cos(np.deg2rad(135))], 
        [0, 4, 0], 
        [3*np.cos(np.deg2rad(135)), 0, 9]]
    )
    assert np.allclose(g, expected)

def test_metric_tensor_for_tetragonal_lattice():
    lp = LatticeParameters(1, 1, 2, 90, 90, 90)
    g = metric_tensor(lp)
    expected = ([[1, 0, 0], [0, 1, 0], [0, 0, 4]])
    assert np.allclose(g, expected)


def test_metric_tensor_for_orthorhombic_lattice():
    lp = LatticeParameters(1, 2, 3, 90, 90, 90)
    g = metric_tensor(lp)
    expected = ([[1, 0, 0], [0, 4, 0], [0, 0, 9]])
    assert np.allclose(g, expected)


def test_metric_tensor_for_rhombohedral_lattice():
    lp = LatticeParameters(1, 1, 1, 110, 110, 110)
    g = metric_tensor(lp)
    cos_alpha = np.cos(np.deg2rad(110))
    expected = ([
        [1, cos_alpha, cos_alpha],
        [cos_alpha, 1, cos_alpha],
        [cos_alpha, cos_alpha, 1]
    ])
    assert np.allclose(g, expected)


# From example 4.3.1 pg.82 of "Structure of Materials"
def test_metric_tensor_value_1():
    lp = LatticeParameters(3, 4, 6, 90, 120, 90)
    g = metric_tensor(lp)
    expected = np.array([[9, 0, -9], [0, 16, 0], [-9, 0, 36]])
    assert np.allclose(g, expected)


# From example 4.3.2 pg.83 of "Structure of Materials"
def test_metric_tensor_value_2():
    lp = LatticeParameters(2, 2, 3, 90, 90, 90)
    g = metric_tensor(lp)
    expected = np.array([[4, 0, 0], [0, 4, 0], [0, 0, 9]])
    assert np.allclose(g, expected)

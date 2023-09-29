"""test_metric_tensor.py"""


import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.metric_tensor import metric_tensor


def test_metric_tensor_for_cubic_crystal():
    lp = LatticeParameters(1, 1, 1, 90, 90, 90)
    g = metric_tensor(lp)
    expected = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert np.allclose(g, expected) == True

"""interplanar_calculations.py"""

import numpy as np

from crystal_visualizer.hkl import HKL
from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.reciprocal_metric_tensor import reciprocal_metric_tensor


def interplanar_distance(
    hkl: HKL, 
    lattice_parameters: LatticeParameters
) -> float:
    indices = np.array([hkl.h, hkl.k, hkl.l])
    g = reciprocal_metric_tensor(lattice_parameters)    
    g_length = np.sqrt(indices @ (g @ indices))
    print(g_length)
    return 1/g_length


def interplanar_angle(
    hkl_1: HKL, 
    hkl_2: HKL, 
    lattice_parameters: LatticeParameters
) -> float:
    """
    Returns the angle between two planes in degrees.
    
    (define plane normals etc)

    """
    pass

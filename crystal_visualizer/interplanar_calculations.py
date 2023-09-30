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
    p = np.array([hkl_1.h, hkl_1.k, hkl_1.l])
    q = np.array([hkl_2.h, hkl_2.k, hkl_2.l])
    g = reciprocal_metric_tensor(lattice_parameters)

    # Intermediate array that contains 3 necessary dot products
    m = np.array([p, q]) @ (g @ np.transpose(np.array(p, q])))
    p_dot_q = m[0, 1]
    p_dot_p = m[0, 0]
    q_dot_q = m[1, 1]

    interplanar_angle = np.arccos(p_dot_p / np.sqrt(p_dot_p * q_dot_q)
    return np.rad2deg(interplanar_angle)
    
    

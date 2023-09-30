"""interplanar_calculations.py"""

import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.reciprocal_metric_tensor import metric_tensor



def interplanar_spacing(hkl: HKL, lattice_parameters: LatticeParameters):
# takes h,k,l and lattice parameters
# uses reciprocal metric tensor
# outputs a float




def interplanar_angle(
    hkl_1: HKL, 
    hkl_2: HKL, 
    lattice_parameters: LatticeParameters
) -> float:
    """
    Returns the angle between two planes in degrees.
    
    (define plane normals etc)

    """

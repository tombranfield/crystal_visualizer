"""reciprocal_metric_tensor.py"""

import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters


def reciprocal_metric_tensor(lattice_parameters: LatticeParameters) -> np.array:
    """
    A function representing a reciprocal metric tensor.

    Aids in the computation of interplanar distances, interplanar angles, and
    the length of reciprocal lattice vectors.

    See Chapter 6 of "Structure of Materials" (De Graef, McHenry, 2012) for
    more information.

    Input:
        lattice parameters held in LatticeParameters class. Note the direct
        space parameters are used, not the reciprocal space parameters.
    Output:
        3x3 numpy ndarray of dtype float64
    """



def volume(lattice_parameters: LatticeParameters) -> float:
    """
    Calculates the direct space volume of a unit cell of a lattice.
    """
    a = lattice_parameters.length_a
    b = lattice_parameters.length_b
    c = lattice_parameters.length_c
    alpha = np.deg2rad(lattice_parameters.angle_alpha)
    beta = np.deg2rad(lattice_parameters.angle_beta)
    gamma = np.deg2rad(lattice_parameters.angle_gamma)

    V_squared = a*a * b*b * c*c * [1 - np.cos(alpha)*np.cos(alpha)
                - np.cos(beta) * np.cos(beta) - np.cos(gamma) * np.cos(gamma)
                + 2 * np.cos(alpha) * np.cos(beta) * np.cos(gamma)]

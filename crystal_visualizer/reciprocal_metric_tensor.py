"""reciprocal_metric_tensor.py"""

import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters


def reciprocal_metric_tensor(lattice_parameters: LatticeParameters) -> np.array:
    """
    A function representing a reciprocal metric tensor.

    Aids in the computation of interplanar distances, interplanar angles, and
    the length of reciprocal lattice vectors.

    See Chapter 6 of "Structure of Materials" (De Graef, McHenry, 2012) for
    more information; page 111 contains the general (triclinic) expression that
    is implemented.

    Input:
        lattice parameters held in LatticeParameters class. Note the direct
        space parameters are used, not the reciprocal space parameters.
    Output:
        3x3 numpy ndarray of dtype float64
    """
    a = lattice_parameters.length_a
    b = lattice_parameters.length_b
    c = lattice_parameters.length_c
    # numpy uses radians for trigonometric values
    alpha = np.deg2rad(lattice_parameters.angle_alpha)
    beta = np.deg2rad(lattice_parameters.angle_beta)
    gamma = np.deg2rad(lattice_parameters.angle_gamma)

    g = np.array([
        [b*b*c*c*np.sin(alpha)**2, a*b*c*c*F(alpha, beta, gamma), a*b*b*c*F(gamma, alpha, beta)],
        [a*b*c*c*F(alpha, beta, gamma), a*a*c*c*np.sin(beta)**2, a*a*b*c*F(beta, gamma, alpha)],
        [a*b*b*c*F(gamma, alpha, beta), a*a*b*c*F(beta, gamma, alpha), a*a*b*b*np.sin(gamma)**2]
    ])
    V = volume(lattice_parameters)
    return g / V ** 2


def F(angle_a, angle_b, angle_c):
    """
    A helper function for a more compact readable reciprocal metric tensor."""
    return np.cos(angle_a) * np.cos(angle_b) - np.cos(angle_c)


def volume(lp: LatticeParameters) -> float:
    """
    Calculates the direct space volume of a unit cell of a lattice.

    See pg.111 of "Structure of Materials" (De Graef, McHenry, 2012) for
    the equation used.
    """
    alpha = np.deg2rad(lp.angle_alpha)
    beta = np.deg2rad(lp.angle_beta)
    gamma = np.deg2rad(lp.angle_gamma)
    V_squared = lp.length_a**2 * lp.length_b**2 * lp.length_c**2 * (1
                - (np.cos(alpha))**2 - (np.cos(beta))**2
                - (np.cos(gamma))**2
                + 2 * np.cos(alpha) * np.cos(beta) * np.cos(gamma))
    return np.sqrt(V_squared)


if __name__ == "__main__":
    lattice_parameters = LatticeParameters(2, 3, 4, 90, 90, 90)
    print(volume(lattice_parameters))

    lattice_parameters = LatticeParameters(10, 10, 10, 90, 90, 90)
    print(volume(lattice_parameters))

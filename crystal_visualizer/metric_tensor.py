"""metric_tensor.py"""

import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters


def MetricTensor(lattice_parameters: LatticeParameters) -> np.array:
    """
    A function representing a metric tensor for crystallographic computations.

    The metric tensor defines the geometrical characteristics of the reference
    frame. It helps computations involving bond distances or angles.

    See Chapter 4 of "Structure of Materials" (De Graef, McHenry, 2012) for
    more information.

    Input: 
        lattice parameters held in LatticeParameters class
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

    # Note is possible to define simplified expressions for the metric
    # tensor for different crystal systems, however have choosen not
    # to use them as would increase complexity of the program for little
    # computational gain.
    g = np.array([
        [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
        [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)],
        [c*a*np.cos(beta), c*b*np.cos(alpha), c*c]
    ])
    return g


if __name__ == "__main__":
    lp = LatticeParameters(4, 6, 5, 90, 120, 90)
    g = MetricTensor(lp)
    r1 = np.array([[1, 0, 1], [-2, 0, 1]])
    r2 = np.array([[1, -2], [0, 1], [1, 1]])
    nu = r1 @ g @ r2
    print(nu)

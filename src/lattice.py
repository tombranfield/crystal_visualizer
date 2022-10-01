"""
A module containing classes that represent the lattice.

The lattice is a infinite periodic array of points in space. For the purpose of
this program, only 3D lattices are used. Please see a typical reference such as
"Structure and Dynamics" (Dove, 2001) or "The Structures of Crystals" (Glazer,
1987) for more information.
"""

class Lattice:
    """
    A class representing a three-dimensional lattice.

    Args:
        length_a, length_b, length_c: floating point numbers representing the
        magnitude (length) of the corresponding basic vectors in Angstroms.
        angle_alpha, angle_beta, angle_gamma: floating-point numbers representing
        the angle between the basis vectors b and c, a and c, and a and b,
        respectively.
    """
    def __init__(self, length_a, length_b, length_c,
                        angle_alpha, angle_beta, angle_gamma):
        """Initialize the lattice using its lattice parameters"""
        self.length_a = length_a
        self.length_b = length_b
        self.length_c = length_c
        self.angle_alpha = angle_alpha
        self.angle_beta = angle_beta
        self.angle_gamma = angle_gamma

    @property
    


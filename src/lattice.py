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
        respectively. In radians (NOT degrees).
    """
    def __init__(self, a, b, c, alpha, beta, gamma):
        """Initialize the lattice using its lattice parameters. """
        self.length_a = a
        self.length_b = b
        self.length_c = c
        self.angle_alpha = alpha
        self.angle_beta = beta
        self.angle_gamma = gamma

    @property
    def length_a(self):
        """Returns the length of basis vector a"""
        return self._a

    @length_a.setter
    def length_a(self, new_length: float):
        """Verifies and sets a new length for the basis vector a"""
        self.__verify_lattice_vector_length(new_length)
        self._a = new_length

    def __verify_lattice_vector_length(self, new_length):
        """Verifies that a given input is a valid length for a lattice vector.

        If the input is valid, no action is taken. Otherwise, an appropriate
        exception is raised.
        """
        if not isinstance(new_length, (float, int)):
            raise TypeError("Lattice length must be a number")
        if new_length <= 0:
            raise ValueError("Lattice length must a positive number")

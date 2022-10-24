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
        a, b, c: floating point numbers representing the
        magnitude (length) of the corresponding basic vectors in Angstroms.
        alpha, beta, gamma: floating-point numbers representing
        the angle between the basis vectors b and c, a and c, and a and b,
        respectively. In radians (NOT degrees).
    """
    def __init__(self, a, b, c, alpha, beta, gamma):
        """Initialize the lattice using its lattice parameters.

        We use single letters to represent the lengths of the basis vectors
        as this is done by convention for crystallography.
        """
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    @property
    def a(self):
        """Returns the length of basis vector a"""
        return self._a

    @a.setter
    def a(self, new_length: float):
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

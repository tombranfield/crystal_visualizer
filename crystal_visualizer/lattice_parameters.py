"""lattice_parameters.py"""


class LatticeParameters:
    """
    A class representing the lattice parameters of a 3D lattice.

    Args:
        len_a, len_b, len_c are the lengths a, b, and c of the lattice vectors
        in Angstroms. These vectors are defined by a right-hand rule by
        convention. See eg "Structure of Materials" (2012).

        angle_alpha, angle_beta, and angle_gamma are the angles alpha, beta, 
        and gamma of the lattice in degrees (NOT radians). Alpha is the angle 
        between b and c, beta the angle between a and c, and gamma the is angle
        between a and b.
    """
    def __init__(self, len_a, len_b, len_c, angle_alpha, angle_beta, angle_gamma):
        self.__verify_length(len_a, len_b, len_c)
        self.__verify_angle(angle_alpha, angle_beta, angle_gamma)
        self._len_a = len_a
        self._len_b = len_b
        self._len_c = len_c
        self._angle_alpha = angle_alpha
        self._angle_beta = angle_beta
        self._angle_gamma = angle_gamma

    @property
    def length_a(self):
        return self._len_a

    @length_a.setter
    def length_a(self, new_length):
        """Verifies and sets a new length for the basis vector a"""
        self.__verify_length(new_length)
        self._len_a = new_length

    def __verify_length(self, *lengths):
        """
        Verifies that a given input is a valid length for the lattice. If the
        input is not valid, an appropriate exception is raised.
        """
        for length in lengths:
            if not isinstance(length, (float, int)):
                raise TypeError("Length must be a number")
            if length <= 0:
                raise ValueError("Length must be a positive number")

    def __verify_angle(self, *angles):
        """
        Verifies that a given input is a valid angle for the lattice. An
        appropriate exception is raised if it is not.

        Note that this does not verify that the angles are in the correct units
        (degrees).
        """
        for angle in angles:
            if not isinstance(angle, (float, int)):
                raise TypeError("Angle must be a number")
            if angle <= 0:
                raise ValueError("Angle must be a positive number")

if __name__ == "__main__":
    my_lattice = LatticeParameters(1, 1, 1, 90, 90, 90)

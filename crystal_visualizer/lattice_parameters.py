"""lattice_parameters.py"""



class LatticeParameters:
    """
    A class representing the lattice parameters of a 3D lattice.

    Args:
        len_a, len_b, len_c are the lengths 
    """
    def __init__(
        self, 
        len_a, len_b, len_c, 
        angle_alpha, angle_beta, angle_gamma
    ):
        self._len_a = len_a
        self._len_b = len_b
        self._len_c = len_c
        self._angle_alpha = angle_alpha
        self._angle_beta = angle_beta
        self._angle_gamma = angle_gamma

    @property
    def length_a(self):
        return self._len_a



    def __verify_length(self, length):
        if not isinstance(length, (float, int)):
            raise TypeError("Length must be a number")
        if length <= 0:
            raise ValueError("Length must be a positive number")


if __name__ == "__main__":
    print("yo")

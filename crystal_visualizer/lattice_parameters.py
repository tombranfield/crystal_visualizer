"""lattice_parameters.py"""



class LatticeParameters:
    """
    Represents the lattice parameters of the lattice.
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


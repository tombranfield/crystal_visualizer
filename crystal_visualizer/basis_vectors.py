"""basis_vectors.py"""


import numpy as np

from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.lattice_parameters import LatticeParameters


class BasisVectors:
    """
    Basis vectors for the lattice
    """

    def __init__(self, lattice_parameters: LatticeParameters):
        self._len_a = lattice_parameters.length_a
        self._len_b = lattice_parameters.length_b
        self._len_c = lattice_parameters.length_c
        # Numpy uses radians, not degrees
        self._alpha = np.deg2rad(lattice_parameters.angle_alpha)
        self._beta = np.deg2rad(lattice_parameters.angle_beta)
        self._gamma = np.deg2rad(lattice_parameters.angle_gamma)
        self._NUM_DP = 8

    @property
    def a(self):
        return np.array([self._len_a, 0, 0])        

    @property 
    def b(self):
        b1 = self._len_b * np.cos(self._gamma)
        b2 = self._len_b * np.sin(self._gamma)
        b3 = 0.0
        b1 = round(b1, self._NUM_DP)
        b2 = round(b2, self._NUM_DP)
        return np.array([b1, b2, b3])

    @property
    def c(self):
        c1 = self._len_c * np.cos(self._beta)
        c2 = ((np.cos(self._alpha) - np.cos(self._beta) * np.cos(self._gamma))
             / np.sin(self._gamma)) * self._len_c

        bracketed = ((np.cos(self._alpha) - np.cos(self._beta) * np.cos(self._gamma))
                    / np.sin(self._gamma))
        c3 = self._len_c * np.sqrt(1 - np.cos(self._beta) ** 2 - bracketed ** 2)
        c1 = round(c1, self._NUM_DP)
        c2 = round(c2, self._NUM_DP)
        c3 = round(c3, self._NUM_DP)
        return np.array([c1, c2, c3])


if __name__ == "__main__":
    cif_reader = CifReader("SiO2.cif")
    lp = cif_reader.lattice_parameters
    basis_vectors = BasisVectors(lp)

    print(lp.length_a)
    print(lp.length_b)
    print(lp.length_c)
    print(lp.angle_alpha)
    print(lp.angle_beta)
    print(lp.angle_gamma)

    print(basis_vectors.a)
    print(basis_vectors.b)
    print(basis_vectors.c)

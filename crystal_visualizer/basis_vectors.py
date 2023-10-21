"""basis_vectors.py"""


import numpy as np

from crystal_visualizer.lattice_parameters import LatticeParameters


class BasisVectors:
    """
    Basis vectors for the lattice
    """
    def __init__(self, lattice_parameters: LatticeParameters):
        self._len_a = lattice_parameters.length_a
        self._len_b = lattice_parameters.length_b
        self._len_c = lattice_parameters.length_c
        self._ang_alpha = lattice_parameters.angle_alpha
        self._ang_beta = lattice_parameters.angle_alpha
        self._ang_gamma = lattice_parameters.angle_alpha


    @property
    def a(self):
        return np.array([self._len_a, 0, 0])        


    @property 
    def b(self):
        x = self._len_b * np.cos(self.ang_gamma)
        y = self._len_b * np.sin(self.ang_gamma)


if __name__ == "__main__":
    lp = LatticeParameters(3.8, 3.9, 4.0, 90.0, 90.0, 90.0)
    basis_vectors = BasisVectors(lp)

    print(basis_vectors.a)

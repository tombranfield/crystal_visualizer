"""test_basis_vectors.py"""


import numpy as np
import pytest

from crystal_visualizer.basis_vectors import BasisVectors
from crystal_visualizer.cif_reader import CifReader



@pytest.mark.current
def test_generate_correct_basis_vectors_for_SrTiO3():
    cif_reader = CifReader("SrTiO3.cif")
    basis_vectors = BasisVectors(cif_reader.lattice_parameters)
    cell_length = cif_reader.lattice_parameters.length_a
    assert np.array_equal(basis_vectors.a, [cell_length, 0.0, 0.0])
    assert np.array_equal(basis_vectors.b, [0, cell_length, 0.0])
    assert np.array_equal(basis_vectors.c, [0, 0, cell_length])

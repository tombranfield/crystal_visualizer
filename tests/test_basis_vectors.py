"""test_basis_vectors.py"""


import numpy as np
import pytest

from crystal_visualizer.basis_vectors import BasisVectors
from crystal_visualizer.cif_reader import CifReader


# Using SrTiO3 as has cubic cell with orthogonal axes of equal lengths
def test_generate_correct_basis_vectors_for_SrTiO3():
    cif_reader = CifReader("SrTiO3.cif")
    basis_vectors = BasisVectors(cif_reader.lattice_parameters)
    cell_length = cif_reader.lattice_parameters.length_a
    assert np.array_equal(basis_vectors.a, [cell_length, 0.0, 0.0])
    assert np.array_equal(basis_vectors.b, [0, cell_length, 0.0])
    assert np.array_equal(basis_vectors.c, [0, 0, cell_length])


# SiO2 has non-orthogonal axes
# We calculate the correct expected values by hand
def test_generate_correct_basis_vectors_for_SiO2():
    cif_reader = CifReader("SiO2.cif")
    basis_vectors = BasisVectors(cif_reader.lattice_parameters)
    expected_a = [4.9019, 0, 0]
    expected_b = [-2.45095, 4.2452, 0]
    expected_c = [0, 0, 5.3988]
    assert np.allclose(basis_vectors.a, expected_a)
    assert np.allclose(basis_vectors.b, expected_b)
    assert np.allclose(basis_vectors.c, expected_c)

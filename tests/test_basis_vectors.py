"""test_basis_vectors.py"""


from crystal_visualizer.basis_vectors import BasisVectors
from crystal_visualizer.cif_reader import CifReader



@pytest.mark.current
def test_generate_correct_basis_vectors_for_SrTiO3():
    cif_reader = CifReader("SrTiO3.cif")
    basis_vectors = BasisVectors(cif_reader.lattice_parameters)
    print(basis_vectors.a)
    print(basis_vectors.b)
    print(basis_vectors.c)

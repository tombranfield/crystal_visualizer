"""test_cif_reader.py"""


import numpy as np
from pathlib import Path
import pytest

from crystal_visualizer.cif_reader import CifReader


CIF_PATH = str( Path(__file__).parents[1] / "data" / "cif_files")



@pytest.mark.current
def test_read_correct_atom_sites_for_copper():
    cif_reader = CifReader("Cu.cif")
    assert len(cif_reader.atoms) == 1
    for atom in cif_reader.atoms:
        assert atom.symbol == "Cu"
        generated_position = atom.position_vector()
        expected_position = np.array([0.0, 0.0, 0.0])
        assert np.array_equal(generated_position, expected_position)


def test_read_correct_atom_sites_for_CaF2():
    cif_reader = CifReader("CaF2.cif")
    assert len(cif_reader.atoms) == 2
    assert cif_reader.atoms[0].symbol == "Ca"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.5, 0.5, 0.5]))
    assert cif_reader.atoms[1].symbol == "F"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0.25, 0.75, 0.75]))


def test_read_correct_atom_sites_for_NaCl():
    cif_reader = CifReader("NaCl.cif")
    assert len(cif_reader.atoms) == 2
    assert cif_reader.atoms[0].symbol == "Na"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0., 0., 0.]))
    assert cif_reader.atoms[1].symbol == "Cl"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0.5, 0.5, 0.5]))


def test_read_correct_atom_sites_for_diamond():
    cif_reader = CifReader("C.cif")
    assert len(cif_reader.atoms) == 1
    assert cif_reader.atoms[0].symbol == "C"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.96, 0.96, 0.96]))
   



def test_generate_correct_lattice_parameters_for_copper():
    cif_reader = CifReader("Cu.cif")
    assert cif_reader.lattice_parameters.length_a == 3.59127
    assert cif_reader.lattice_parameters.length_b == 3.59127
    assert cif_reader.lattice_parameters.length_c == 3.59127
    assert cif_reader.lattice_parameters.angle_alpha == 90.0
    assert cif_reader.lattice_parameters.angle_beta == 90.0
    assert cif_reader.lattice_parameters.angle_gamma == 90.0


def test_generate_correct_lattice_parameters_for_NaCl():
    cif_reader = CifReader("NaCl.cif")
    assert cif_reader.lattice_parameters.length_a == 5.62
    assert cif_reader.lattice_parameters.length_b == 5.62
    assert cif_reader.lattice_parameters.length_c == 5.62
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_CaF2():
    cif_reader = CifReader("CaF2.cif")
    assert cif_reader.lattice_parameters.length_a == 5.45095
    assert cif_reader.lattice_parameters.length_b == 5.45095
    assert cif_reader.lattice_parameters.length_c == 5.45095
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_diamond():
    cif_reader = CifReader("C.cif")
    assert cif_reader.lattice_parameters.length_a == 3.54
    assert cif_reader.lattice_parameters.length_b == 3.54
    assert cif_reader.lattice_parameters.length_c == 3.54
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_CsCl():
    cif_reader = CifReader("CsCl.cif")
    assert cif_reader.lattice_parameters.length_a == 4.123
    assert cif_reader.lattice_parameters.length_b == 4.123
    assert cif_reader.lattice_parameters.length_c == 4.123
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_spinel():
    cif_reader = CifReader("MgAl2O4.cif")
    assert cif_reader.lattice_parameters.length_a == 8.2065
    assert cif_reader.lattice_parameters.length_b == 8.2065
    assert cif_reader.lattice_parameters.length_c == 8.2065
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_quartz():
    cif_reader = CifReader("SiO2.cif")
    assert cif_reader.lattice_parameters.length_a == 4.9019
    assert cif_reader.lattice_parameters.length_b == 4.9019
    assert cif_reader.lattice_parameters.length_c == 5.3988
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 120


def test_generate_correct_lattice_parameters_for_perovskite():
    cif_reader = CifReader("SrTiO3.cif")
    assert cif_reader.lattice_parameters.length_a == 3.899
    assert cif_reader.lattice_parameters.length_b == 3.899
    assert cif_reader.lattice_parameters.length_c == 3.899
    assert cif_reader.lattice_parameters.angle_alpha == 90.0
    assert cif_reader.lattice_parameters.angle_beta == 90.0
    assert cif_reader.lattice_parameters.angle_gamma == 90


def test_generate_correct_lattice_parameters_for_YBCO():
    cif_reader = CifReader("YBa2Cu3O7-x.cif")
    assert cif_reader.lattice_parameters.length_a == 3.8203
    assert cif_reader.lattice_parameters.length_b == 3.88548
    assert cif_reader.lattice_parameters.length_c == 11.68349
    assert cif_reader.lattice_parameters.angle_alpha == 90
    assert cif_reader.lattice_parameters.angle_beta == 90
    assert cif_reader.lattice_parameters.angle_gamma == 90



if __name__ == "__main__":
    print(CIF_PATH)

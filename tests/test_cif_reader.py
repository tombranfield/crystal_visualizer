"""test_cif_reader.py"""


import numpy as np
from pathlib import Path
import pytest

from crystal_visualizer.cif_reader import CifReader


CIF_PATH = str( Path(__file__).parents[1] / "data" / "cif_files")



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
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.125, 0.125, 0.125]))
   

def test_read_correct_atom_sites_for_spinel():
    cif_reader = CifReader("MgAl2O4.cif")
    assert len(cif_reader.atoms) == 3
    assert cif_reader.atoms[0].symbol == "Mg"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0., 0., 0.]))
    assert cif_reader.atoms[1].symbol == "Al"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0.625, 0.625, 0.625]))
    assert cif_reader.atoms[2].symbol == "O"
    assert np.array_equal(cif_reader.atoms[2].position_vector(), np.array([0.3855, 0.3855, 0.3855]))
    

def test_read_correct_atom_sites_for_perovskite():
    cif_reader = CifReader("SrTiO3.cif")
    assert len(cif_reader.atoms) == 3
    assert cif_reader.atoms[0].symbol == "Sr"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.5, 0.5, 0.5]))
    assert cif_reader.atoms[1].symbol == "Ti"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0., 0., 0.]))
    assert cif_reader.atoms[2].symbol == "O"
    assert np.array_equal(cif_reader.atoms[2].position_vector(), np.array([0.5, 0., 0.]))


def test_read_correct_atom_sites_for_quartz():
    cif_reader = CifReader("SiO2.cif")
    assert len(cif_reader.atoms) == 2
    assert cif_reader.atoms[0].symbol == "O"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.413, 0.2711, 0.2172]))
    assert cif_reader.atoms[1].symbol == "Si"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0.4673, 0., 0.3333]))


def test_read_correct_atom_sites_for_YBCO():
    cif_reader = CifReader("YBa2Cu3O7-x.cif")
    assert len(cif_reader.atoms) == 8
    assert cif_reader.atoms[0].symbol == "Y"
    assert np.array_equal(cif_reader.atoms[0].position_vector(), np.array([0.5, 0.5, 0.5]))
    assert cif_reader.atoms[1].symbol == "Ba"
    assert np.array_equal(cif_reader.atoms[1].position_vector(), np.array([0.5, 0.5, 0.18393]))
    assert cif_reader.atoms[2].symbol == "Cu"
    assert np.array_equal(cif_reader.atoms[2].position_vector(), np.array([0., 0., 0.]))
    assert cif_reader.atoms[3].symbol == "Cu"
    assert np.array_equal(cif_reader.atoms[3].position_vector(), np.array([0., 0., 0.35501]))
    assert cif_reader.atoms[4].symbol == "O"
    assert np.array_equal(cif_reader.atoms[4].position_vector(), np.array([0., 0.5, 0.]))
    assert cif_reader.atoms[5].symbol == "O"
    assert np.array_equal(cif_reader.atoms[5].position_vector(), np.array([0.5, 0., 0.37819]))
    assert cif_reader.atoms[6].symbol == "O"
    assert np.array_equal(cif_reader.atoms[6].position_vector(), np.array([0., 0.5, 0.37693]))
    assert cif_reader.atoms[7].symbol == "O"
    assert np.array_equal(cif_reader.atoms[7].position_vector(), np.array([0., 0., 0.1584]))



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
    assert cif_reader.lattice_parameters.length_a == 3.566636
    assert cif_reader.lattice_parameters.length_b == 3.566636
    assert cif_reader.lattice_parameters.length_c == 3.566636
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


def test_generate_correct_number_of_symmetry_ops_for_Cu():
    cif_reader = CifReader("Cu.cif")
    assert len(cif_reader.symmetry_ops) == 192 


def test_generate_correct_number_of_symmetry_ops_for_NaCl():
    cif_reader = CifReader("NaCl.cif")
    assert len(cif_reader.symmetry_ops) == 192 


def test_generate_correct_number_of_symmetry_ops_for_CaF2():
    cif_reader = CifReader("CaF2.cif")
    assert len(cif_reader.symmetry_ops) == 192 


def test_generate_correct_number_of_symmetry_ops_for_diamond():
    cif_reader = CifReader("C.cif")
    assert len(cif_reader.symmetry_ops) == 192 

def test_generate_correct_number_of_symmetry_ops_for_perovskite():
    cif_reader = CifReader("SrTiO3.cif")
    assert len(cif_reader.symmetry_ops) == 48 


def test_generate_correct_number_of_symmetry_ops_for_spinel():
    cif_reader = CifReader("MgAl2O4.cif")
    assert len(cif_reader.symmetry_ops) == 192 


def test_generate_correct_number_of_symmetry_ops_for_quartz():
    cif_reader = CifReader("SiO2.cif")
    assert len(cif_reader.symmetry_ops) == 6


def test_generate_correct_number_of_symmetry_ops_for_YBCO():
    cif_reader = CifReader("YBa2Cu3O7-x.cif")
    assert len(cif_reader.symmetry_ops) == 8





if __name__ == "__main__":
    print(CIF_PATH)

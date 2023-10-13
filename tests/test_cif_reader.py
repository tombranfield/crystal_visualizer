"""test_cif_reader.py"""


from pathlib import Path
import pytest

from crystal_visualizer.cif_reader import CifReader


CIF_PATH = str( Path(__file__).parents[1] / "data" / "cif_files")


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


if __name__ == "__main__":
    print(CIF_PATH)

"""test_general_pos_generator.py"""


import pytest

from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.general_pos_generator import GeneralPositionGenerator


@pytest.fixture
def cu_atoms():
    cif_reader = CifReader("Cu.cif")
    return cif_reader.atoms

@pytest.fixture
def cu_sym_ops():
    cif_reader = CifReader("Cu.cif")
    return cif_reader.symmetry_ops.sym_ops



def test_can_convert_single_digit_to_float(cu_atoms, cu_sym_ops):
    gps = GeneralPositionGenerator(cu_atoms, cu_sym_ops)
    assert gps.fraction_str_to_float("3") == 3.0

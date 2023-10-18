"""test_general_pos_generator.py"""

import numpy as np
import pytest

from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.general_pos_generator import GeneralPositionsGenerator


@pytest.fixture
def cu_atoms():
    cif_reader = CifReader("Cu.cif")
    return cif_reader.atoms

@pytest.fixture
def cu_sym_ops():
    cif_reader = CifReader("Cu.cif")
    return cif_reader.symmetry_ops.sym_ops


@pytest.fixture
def cu_general_pos_gen(cu_atoms, cu_sym_ops):
    return GeneralPositionsGenerator(cu_atoms, cu_sym_ops)
    

def test_can_convert_single_digit_to_float(cu_general_pos_gen):
    assert cu_general_pos_gen._fraction_str_to_float("3") == 3.0


def test_can_convert_fraction_str_to_float(cu_general_pos_gen):
    assert cu_general_pos_gen._fraction_str_to_float("1/2") == 0.5
    assert cu_general_pos_gen._fraction_str_to_float("3/4") == 0.75


def test_can_convert_negative_fraction_str_to_float(cu_general_pos_gen):
    assert cu_general_pos_gen._fraction_str_to_float("-1/2") == -0.5
    assert cu_general_pos_gen._fraction_str_to_float("-3/4") == -0.75


def test_correctly_generate_cu_atoms():
    cif_reader = CifReader("Cu.cif")
    cu_atom = cif_reader.atoms[0]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositionsGenerator(cu_atom, sym_ops)
    new_positions = general_positions.generate()
    new_coods_list = []
    for new_pos in new_positions:
        new_coods_list.append(new_pos.coods())
    new_coods_list = [list(arr) for arr in new_coods_list]
    assert len(new_coods_list) == 14
    assert [0., 0., 0.] in new_coods_list
    assert [0., 0., 1.] in new_coods_list
    assert [0., 1., 0.] in new_coods_list
    assert [0., 1., 1.] in new_coods_list
    assert [1., 0., 0.] in new_coods_list
    assert [1., 0., 1.] in new_coods_list
    assert [1., 1., 0.] in new_coods_list
    assert [1., 1., 1.] in new_coods_list
    assert [0., 0.5, 0.5] in new_coods_list
    assert [1.0, 0.5, 0.5] in new_coods_list
    assert [0.5, 0., 0.5] in new_coods_list
    assert [0.5, 1.0, 0.5] in new_coods_list
    assert [0.5, 0.5, 0.] in new_coods_list
    assert [0.5, 0.5, 1.] in new_coods_list

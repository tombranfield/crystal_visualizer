"""test_general_pos_generator.py"""

import numpy as np
import pytest

from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.general_pos_generator import GeneralPositionsGenerator



def generate_and_test_pos(atom, sym_ops, expected_positions):
    pos_gen = GeneralPositionsGenerator(atom, sym_ops)
    gen_positions = pos_gen.generate_positions()
    gen_coods = []
    for gen_pos in gen_positions:
        gen_coods.append(gen_pos.coods())
    gen_coods = [list(arr) for arr in gen_coods]
    assert len(gen_coods) == len(expected_positions)
    for expected_pos in expected_positions:
        assert expected_pos in gen_coods


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


def test_correctly_generate_Cu_atom_positions():
    cif_reader = CifReader("Cu.cif")
    Cu_atom = cif_reader.atoms[0]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Cu_positions = [
        [0., 0., 0.],    [0., 0., 1.],   [0., 1., 0.],
        [0., 1., 1.],    [1., 0., 0.],   [1., 0., 1.],
        [1., 1., 0.],    [1., 1., 1.],   [0., 0.5, 0.5],
        [1.0, 0.5, 0.5], [0.5, 0., 0.5], [0.5, 1.0, 0.5],
        [0.5, 0.5, 0.],  [0.5, 0.5, 1.] 
    ]

    generate_and_test_pos(Cu_atom, sym_ops, expected_Cu_positions)


def test_correctly_generate_NaCl_atom_positions():
    cif_reader = CifReader("NaCl.cif")
    Na_atom = cif_reader.atoms[0]
    Cl_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Na_positions = [
        [0., 0., 0.], [0., 0., 1.], [0., 1., 0.],
        [0., 1., 1.], [1., 0., 0.], [1., 0., 1.],
        [1., 1., 0.], [1., 1., 1.], [0., 0.5, 0.5],
        [1., 0.5, 0.5], [0.5, 0., 0.5], [0.5, 1., 0.5],
        [0.5, 0.5, 0.], [0.5, 0.5, 1.]
    ]    
    expected_Cl_positions = [
        [0.5, 0.5, 0.5], [0.5, 0., 0.],  [0.5, 0., 1.],
        [0.5, 1., 0.],   [0.5, 1., 1.],  [0., 0.5, 0.],
        [0., 0.5, 1.],   [1., 0.5, 0.],  [1., 0.5, 1.],
        [0., 0., 0.5],   [0., 1., 0.5],  [1., 0., 0.5],
        [1., 1., 0.5]
    ]

    generate_and_test_pos(Na_atom, sym_ops, expected_Na_positions)
    generate_and_test_pos(Cl_atom, sym_ops, expected_Cl_positions)



def test_correctly_generate_CaF2_atom_positions():
    cif_reader = CifReader("CaF2.cif")
    Ca_atom = cif_reader.atoms[0]
    F_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Ca_positions = [
        [0.5, 0.5, 0.5], [0.5, 0., 0.],  [0.5, 0., 1.],
        [0.5, 1., 0.],   [0.5, 1., 1.],  [0., 0.5, 0.],
        [0., 0.5, 1.],   [1., 0.5, 0.],  [1., 0.5, 1.],
        [0., 0., 0.5],   [0., 1., 0.5],  [1., 0., 0.5],
        [1., 1., 0.5]
    ]

    expected_F_positions = [
        [0.25, 0.75, 0.75], [0.75, 0.25, 0.25], [0.75, 0.25, 0.75],
        [0.25, 0.75, 0.25], [0.75, 0.75, 0.25], [0.25, 0.25, 0.75],
        [0.25, 0.25, 0.25], [0.75, 0.75, 0.75]
    ]

    generate_and_test_pos(Ca_atom, sym_ops, expected_Ca_positions)
    generate_and_test_pos(F_atom, sym_ops, expected_F_positions)


def test_correctly_generate_SrTiO3_atom_positions():
    cif_reader = CifReader("SrTiO3.cif")
    Sr_atom = cif_reader.atoms[0]
    Ti_atom = cif_reader.atoms[1]
    O_atom = cif_reader.atoms[2]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Sr_positions = [[0.5, 0.5, 0.5]]
    expected_Ti_positions = [
        [0., 0., 0.], [0., 0., 1.], [0., 1., 0.],
        [0., 1., 1.], [1., 0., 0.], [1., 0., 1.],
        [1., 1., 0.], [1., 1., 1.]
    ]
    expected_O_positions = [
        [0.5, 0., 0.], [0.5, 0., 1.], [0.5, 1., 0.],
        [0.5, 1., 1.], [0., 0.5, 0.], [0., 0.5, 1.],
        [1., 0.5, 0.], [1., 0.5, 1.], [0., 0., 0.5],
        [0., 1., 0.5], [1., 0., 0.5], [1., 1., 0.5]
    ]

    generate_and_test_pos(Sr_atom, sym_ops, expected_Sr_positions)
    generate_and_test_pos(Ti_atom, sym_ops, expected_Ti_positions)
    generate_and_test_pos(O_atom, sym_ops, expected_O_positions)


def test_correctly_generate_MgAl2O4_atom_positions():
    cif_reader = CifReader("MgAl2O4.cif")
    Mg_atom = cif_reader.atoms[0]
    Al_atom = cif_reader.atoms[1]
    O_atom = cif_reader.atoms[2]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Mg_positions = [
        [0., 0., 0.],       [0., 0., 1.],       [0., 1., 0.],
        [0., 1., 1.],       [1., 0., 0.],       [1., 0., 1.],
        [1., 1., 0.],       [1., 1., 1.],       [0., 0.5, 0.5],
        [1., 0.5, 0.5],     [0.5, 0.5, 0.],     [0.5, 0.5, 1.],
        [0.5, 0., 0.5],     [0.5, 1., 0.5],     [0.75, 0.25, 0.75],
        [0.25, 0.25, 0.25], [0.25, 0.75, 0.75], [0.75, 0.75, 0.25]
    ]
    expected_Al_positions = [
        [0.625, 0.625, 0.625], [0.375, 0.875, 0.125], 
        [0.875, 0.125, 0.375], [0.125, 0.375, 0.875], 
        [0.875, 0.375, 0.125], [0.375, 0.125, 0.875], 
        [0.125, 0.875, 0.375], [0.625, 0.125, 0.125], 
        [0.375, 0.375, 0.625], [0.875, 0.625, 0.875], 
        [0.875, 0.875, 0.625], [0.375, 0.625, 0.375], 
        [0.125, 0.625, 0.125], [0.625, 0.375, 0.375], 
        [0.625, 0.875, 0.875], [0.125, 0.125, 0.625]
    ]
    expected_O_positions = [
        [0.3855, 0.3855, 0.3855], [0.6145, 0.1145, 0.8855],
        [0.1145, 0.8855, 0.6145], [0.8855, 0.6145, 0.1145],
        [0.1355, 0.6355, 0.3645], [0.8645, 0.8645, 0.8645],
        [0.6355, 0.3645, 0.1355], [0.3645, 0.1355, 0.6355],
        [0.6355, 0.1355, 0.3645], [0.1355, 0.3645, 0.6355],
        [0.3645, 0.6355, 0.1355], [0.1145, 0.6145, 0.8855],
        [0.6145, 0.8855, 0.1145], [0.8855, 0.1145, 0.6145],
        [0.3855, 0.8855, 0.8855], [0.6145, 0.6145, 0.3855],
        [0.1145, 0.3855, 0.1145], [0.1355, 0.1355, 0.8645],
        [0.8645, 0.3645, 0.3645], [0.6355, 0.8645, 0.6355],
        [0.6355, 0.6355, 0.8645], [0.1355, 0.8645, 0.1355],
        [0.1145, 0.1145, 0.3855], [0.6145, 0.3855, 0.6145],
        [0.8855, 0.3855, 0.8855], [0.3855, 0.6145, 0.6145],
        [0.3645, 0.8645, 0.3645], [0.8645, 0.1355, 0.1355],
        [0.8645, 0.6355, 0.6355], [0.3855, 0.1145, 0.1145],
        [0.8855, 0.8855, 0.3855], [0.3645, 0.3645, 0.8645]
    ]

    generate_and_test_pos(Mg_atom, sym_ops, expected_Mg_positions)
    generate_and_test_pos(Al_atom, sym_ops, expected_Al_positions)
    generate_and_test_pos(O_atom, sym_ops, expected_O_positions)



def test_correctly_generate_diamond_atom_positions():
    cif_reader = CifReader("C.cif")
    C_atom = cif_reader.atoms[0]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_C_positions = [
        [0.125, 0.125, 0.125], [0.375, 0.375, 0.875],
        [0.875, 0.375, 0.375], [0.375, 0.875, 0.375],
        [0.125, 0.625, 0.625], [0.625, 0.125, 0.625],
        [0.625, 0.625, 0.125], [0.875, 0.875, 0.875]
    ]

    generate_and_test_pos(C_atom, sym_ops, expected_C_positions)



def test_generate_correct_quartz_atom_positions():
    cif_reader = CifReader("SiO2.cif")
    O_atom = cif_reader.atoms[0]
    Si_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_O_positions = [
        [0.4130, 0.2711, 0.2172], [0.7289, 0.1419, 0.5505],
        [0.8581, 0.5870, 0.8839], [0.2711, 0.4130, 0.7828],
        [0.1419, 0.7289, 0.4495], [0.5870, 0.8581, 0.1161],
    ]
    expected_Si_positions = [
        [0.4673, 0.0000, 0.3333], [0.4673, 1.0000, 0.3333],
        [0.0000, 0.4673, 0.6666], [1.0000, 0.4673, 0.6666],
        [0.5327, 0.5327, 0.0000], [0.5327, 0.5327, 1.0000],
    ]

    generate_and_test_pos(Si_atom, sym_ops, expected_Si_positions)
    generate_and_test_pos(O_atom, sym_ops, expected_O_positions)

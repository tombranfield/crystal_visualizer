"""test_general_pos_generator.py"""

import numpy as np
import pytest

from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.general_pos_generator import GeneralPositionsGenerator
from crystal_visualizer.position import Position


def generate_pos(atom, sym_ops):
    pos_gen = GeneralPositionsGenerator(atom, sym_ops)
    return pos_gen.generate_positions()


def check_generated_positions(gen_positions, expected_coods):
    for expected_cood in expected_coods:
        expected_pos = Position(expected_cood[0], expected_cood[1], expected_cood[2])
        assert is_position_in_position_list(expected_pos, gen_positions)



def is_position_in_position_list(position, positions_list):
    tol = 0.0001
    for existing_pos in positions_list:
        if (abs(position.x - existing_pos.x) <= tol and
            abs(position.y - existing_pos.y) <= tol and
            abs(position.z - existing_pos.z) <= tol
        ):
            return True
    return False


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
    generated_Cu_positions = generate_pos(Cu_atom, sym_ops)
    check_generated_positions(generated_Cu_positions, expected_Cu_positions)


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

    generated_Na_positions = generate_pos(Na_atom, sym_ops)
    generated_Cl_positions = generate_pos(Cl_atom, sym_ops)

    check_generated_positions(generated_Na_positions, expected_Na_positions)
    check_generated_positions(generated_Cl_positions, expected_Cl_positions)






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

    generated_Ca_positions = generate_pos(Ca_atom, sym_ops)
    generated_F_positions = generate_pos(F_atom, sym_ops)

    check_generated_positions(generated_Ca_positions, expected_Ca_positions)
    check_generated_positions(generated_F_positions, expected_F_positions)




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

    generated_Sr_positions = generate_pos(Sr_atom, sym_ops)
    generated_Ti_positions = generate_pos(Ti_atom, sym_ops)
    generated_O_positions = generate_pos(O_atom, sym_ops)

    check_generated_positions(generated_Sr_positions, expected_Sr_positions)
    check_generated_positions(generated_Ti_positions, expected_Ti_positions)
    check_generated_positions(generated_O_positions, expected_O_positions)






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

    generated_Mg_positions = generate_pos(Mg_atom, sym_ops)
    generated_Al_positions = generate_pos(Al_atom, sym_ops)
    generated_O_positions = generate_pos(O_atom, sym_ops)

    check_generated_positions(generated_Mg_positions, expected_Mg_positions)
    check_generated_positions(generated_Al_positions, expected_Al_positions)
    check_generated_positions(generated_O_positions, expected_O_positions)





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

    generated_C_positions = generate_pos(C_atom, sym_ops)

    check_generated_positions(generated_C_positions, expected_C_positions)




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

    generated_Si_positions = generate_pos(Si_atom, sym_ops)
    generated_O_positions = generate_pos(O_atom, sym_ops)

    check_generated_positions(generated_Si_positions, expected_Si_positions)
    check_generated_positions(generated_O_positions, expected_O_positions)


def test_generate_correct_YBCO_atom_positions():
    cif_reader = CifReader("YBa2Cu3O7-x.cif")
    Y_atom = cif_reader.atoms[0]
    Ba_atom = cif_reader.atoms[1]
    Cu_atom_1 = cif_reader.atoms[2]
    Cu_atom_2 = cif_reader.atoms[3]
    O_atom_1 = cif_reader.atoms[4]
    O_atom_2 = cif_reader.atoms[5]
    O_atom_3 = cif_reader.atoms[6]
    O_atom_4 = cif_reader.atoms[7]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    expected_Y_positions = [[0.5, 0.5, 0.5]]

    expected_Ba_positions = [
        [0.5, 0.5, 0.1839],  [0.5, 0.5, 0.8161]
    ]

    expected_Cu_positions = [
        [0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 1.0000],
        [0.0000, 1.0000, 0.0000], [0.0000, 1.0000, 1.0000],
        [1.0000, 0.0000, 0.0000], [1.0000, 0.0000, 1.0000],
        [1.0000, 1.0000, 0.0000], [1.0000, 1.0000, 1.0000],
        [0.0000, 0.0000, 0.3550], [0.0000, 1.0000, 0.3550],
        [1.0000, 0.0000, 0.3550], [1.0000, 1.0000, 0.3550],
        [0.0000, 0.0000, 0.6449], [0.0000, 1.0000, 0.6449],
        [1.0000, 0.0000, 0.6449], [1.0000, 1.0000, 0.6449]
    ]

    expected_O_positions = [
        [0.0000, 0.5000, 0.0000], [0.0000, 0.5000, 1.0000],
        [1.0000, 0.5000, 0.0000], [1.0000, 0.5000, 1.0000],
        [0.5000, 0.0000, 0.3781], [0.5000, 1.0000, 0.3781],
        [0.5000, 0.0000, 0.6218], [0.5000, 1.0000, 0.6218],
        [0.0000, 0.5000, 0.3769], [1.0000, 0.5000, 0.3769],
        [0.0000, 0.5000, 0.6230], [1.0000, 0.5000, 0.6230],
        [0.0000, 0.0000, 0.1584], [0.0000, 1.0000, 0.1584],
        [1.0000, 0.0000, 0.1584], [1.0000, 1.0000, 0.1584],
        [0.0000, 0.0000, 0.8416], [0.0000, 1.0000, 0.8416],
        [1.0000, 0.0000, 0.8416], [1.0000, 1.0000, 0.8416],
    ]

    generated_Y_positions = generate_pos(Y_atom, sym_ops)
    generated_Ba_positions = generate_pos(Ba_atom, sym_ops)

    generated_Cu_positions = []
    for atom in [Cu_atom_1, Cu_atom_2]:
        generated_pos = generate_pos(atom, sym_ops)
        generated_Cu_positions.extend(generated_pos)

    generated_O_positions = []
    for atom in [O_atom_1, O_atom_2, O_atom_3, O_atom_4]:
        generated_pos = generate_pos(atom, sym_ops)
        generated_O_positions.extend(generated_pos)

    check_generated_positions(generated_Y_positions, expected_Y_positions)
    check_generated_positions(generated_Ba_positions, expected_Ba_positions)
    check_generated_positions(generated_Cu_positions, expected_Cu_positions)
    check_generated_positions(generated_O_positions, expected_O_positions)


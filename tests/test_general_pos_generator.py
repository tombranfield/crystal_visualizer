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


def test_correctly_generate_Cu_atom_positions():
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


def test_correctly_generate_NaCl_atom_positions():
    cif_reader = CifReader("NaCl.cif")
    Na_atom = cif_reader.atoms[0]
    Cl_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    Na_general_positions = GeneralPositionsGenerator(Na_atom, sym_ops)
    Na_positions = Na_general_positions.generate()
    assert len(Na_positions) == 14
    Na_coods= []
    for Na_pos in Na_positions:
        Na_coods.append(Na_pos.coods())
    Na_coods = [list(arr) for arr in Na_coods]
    assert [0., 0., 0.] in Na_coods
    assert [0., 0., 1.] in Na_coods
    assert [0., 1., 0.] in Na_coods
    assert [0., 1., 1.] in Na_coods
    assert [1., 0., 0.] in Na_coods
    assert [1., 0., 1.] in Na_coods
    assert [1., 1., 0.] in Na_coods
    assert [1., 1., 1.] in Na_coods
    assert [0., 0.5, 0.5] in Na_coods
    assert [1., 0.5, 0.5] in Na_coods
    assert [0.5, 0., 0.5] in Na_coods
    assert [0.5, 1., 0.5] in Na_coods
    assert [0.5, 0.5, 0.] in Na_coods
    assert [0.5, 0.5, 1.] in Na_coods
    
    Cl_general_positions = GeneralPositionsGenerator(Cl_atom, sym_ops)
    Cl_positions = Cl_general_positions.generate()
    assert len(Cl_positions) == 13
    Cl_coods= []
    for Cl_pos in Cl_positions:
        Cl_coods.append(Cl_pos.coods())
    Cl_coods = [list(arr) for arr in Cl_coods]
    assert [0.5, 0.5, 0.5] in Cl_coods
    assert [0.5, 0., 0.] in Cl_coods
    assert [0.5, 0., 1.] in Cl_coods
    assert [0.5, 1., 0.] in Cl_coods
    assert [0.5, 1., 1.] in Cl_coods
    assert [0., 0.5, 0.] in Cl_coods
    assert [0., 0.5, 1.] in Cl_coods
    assert [1., 0.5, 0.] in Cl_coods
    assert [1., 0.5, 1.] in Cl_coods
    assert [0., 0., 0.5] in Cl_coods
    assert [0., 1., 0.5] in Cl_coods
    assert [1., 0., 0.5] in Cl_coods
    assert [1., 1., 0.5] in Cl_coods




def test_correctly_generate_CaF2_atom_positions():
    cif_reader = CifReader("CaF2.cif")
    Ca_atom = cif_reader.atoms[0]
    F_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    Ca_general_positions = GeneralPositionsGenerator(Ca_atom, sym_ops)
    Ca_positions = Ca_general_positions.generate()
    assert len(Ca_positions) == 13
    Ca_coods= []
    for Ca_pos in Ca_positions:
        Ca_coods.append(Ca_pos.coods())
    Ca_coods = [list(arr) for arr in Ca_coods]
    assert [0.5, 0.5, 0.5] in Ca_coods
    assert [0.5, 0., 0.] in Ca_coods
    assert [0.5, 0., 1.] in Ca_coods
    assert [0.5, 1., 0.] in Ca_coods
    assert [0.5, 1., 1.] in Ca_coods
    assert [0., 0.5, 0.] in Ca_coods
    assert [0., 0.5, 1.] in Ca_coods
    assert [1., 0.5, 0.] in Ca_coods
    assert [1., 0.5, 1.] in Ca_coods
    assert [0., 0., 0.5] in Ca_coods
    assert [0., 1., 0.5] in Ca_coods
    assert [1., 0., 0.5] in Ca_coods
    assert [1., 1., 0.5] in Ca_coods

    F_general_positions = GeneralPositionsGenerator(F_atom, sym_ops)
    F_positions = F_general_positions.generate()
    assert len(F_positions) == 8
    F_coods= []
    for F_pos in F_positions:
        F_coods.append(F_pos.coods())
    F_coods = [list(arr) for arr in F_coods]
    assert [0.25, 0.75, 0.75] in F_coods
    assert [0.75, 0.25, 0.25] in F_coods
    assert [0.75, 0.25, 0.75] in F_coods
    assert [0.25, 0.75, 0.25] in F_coods
    assert [0.75, 0.75, 0.25] in F_coods
    assert [0.25, 0.25, 0.75] in F_coods
    assert [0.25, 0.25, 0.25] in F_coods
    assert [0.75, 0.75, 0.75] in F_coods


def test_correctly_generate_SrTiO3_atom_positions():
    cif_reader = CifReader("SrTiO3.cif")
    Sr_atom = cif_reader.atoms[0]
    Ti_atom = cif_reader.atoms[1]
    O_atom = cif_reader.atoms[2]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    Sr_pos_gen = GeneralPositionsGenerator(Sr_atom, sym_ops)
    Sr_positions = Sr_pos_gen.generate()
    Sr_coods = []
    for Sr_pos in Sr_positions:
        Sr_coods.append(Sr_pos.coods())
    Sr_coods = [list(arr) for arr in Sr_coods]
    assert len(Sr_positions) == 1
    assert [0.5, 0.5, 0.5] in Sr_coods    

    Ti_pos_gen = GeneralPositionsGenerator(Ti_atom, sym_ops)
    Ti_positions = Ti_pos_gen.generate()
    Ti_coods = []
    for Ti_pos in Ti_positions:
        Ti_coods.append(Ti_pos.coods())
    Ti_coods = [list(arr) for arr in Ti_coods]
    assert len(Ti_positions) == 8
    assert [0., 0., 0.] in Ti_coods
    assert [0., 0., 1.] in Ti_coods
    assert [0., 1., 0.] in Ti_coods
    assert [0., 1., 1.] in Ti_coods
    assert [1., 0., 0.] in Ti_coods
    assert [1., 0., 1.] in Ti_coods
    assert [1., 1., 0.] in Ti_coods
    assert [1., 1., 1.] in Ti_coods

    O_pos_gen = GeneralPositionsGenerator(O_atom, sym_ops)
    O_positions = O_pos_gen.generate()
    O_coods = []
    for O_pos in O_positions:
        O_coods.append(O_pos.coods())
    O_coods = [list(arr) for arr in O_coods]
    print(O_coods)
    assert len(O_positions) == 12
    assert [0.5, 0., 0.] in O_coods
    assert [0.5, 0., 1.] in O_coods
    assert [0.5, 1., 0.] in O_coods
    assert [0.5, 1., 1.] in O_coods
    assert [0., 0.5, 0.] in O_coods
    assert [0., 0.5, 1.] in O_coods
    assert [1., 0.5, 0.] in O_coods
    assert [1., 0.5, 1.] in O_coods
    assert [0., 0., 0.5] in O_coods
    assert [0., 1., 0.5] in O_coods
    assert [1., 0., 0.5] in O_coods
    assert [1., 1., 0.5] in O_coods


def test_correctly_generate_MgAl2O4_atom_positions():
    cif_reader = CifReader("MgAl2O4.cif")

    # TODO rewrite below
    Mg_atom = cif_reader.atoms[0]
    Al_atom = cif_reader.atoms[1]
    O_atom = cif_reader.atoms[2]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    Mg_pos_gen = GeneralPositionsGenerator(Mg_atom, sym_ops)
    Mg_positions = Mg_pos_gen.generate()
    Mg_coods = []
    for Mg_pos in Mg_positions:
        Mg_coods.append(Mg_pos.coods())
    Mg_coods = [list(arr) for arr in Mg_coods]
    assert len(Mg_positions) == 18
    assert [0., 0., 0.] in Mg_coods    
    assert [0., 0., 1.] in Mg_coods
    assert [0., 1., 0.] in Mg_coods
    assert [0., 1., 1.] in Mg_coods
    assert [1., 0., 0.] in Mg_coods
    assert [1., 0., 1.] in Mg_coods
    assert [1., 1., 0.] in Mg_coods
    assert [1., 1., 1.] in Mg_coods
    assert [0., 0.5, 0.5] in Mg_coods
    assert [1., 0.5, 0.5] in Mg_coods
    assert [0.5, 0.5, 0.] in Mg_coods
    assert [0.5, 0.5, 1.] in Mg_coods
    assert [0.5, 0., 0.5] in Mg_coods
    assert [0.5, 1., 0.5] in Mg_coods
    assert [0.75, 0.25, 0.75] in Mg_coods
    assert [0.25, 0.25, 0.25] in Mg_coods
    assert [0.25, 0.75, 0.75] in Mg_coods
    assert [0.75, 0.75, 0.25] in Mg_coods

    Al_pos_gen = GeneralPositionsGenerator(Al_atom, sym_ops)
    Al_positions = Al_pos_gen.generate()
    Al_coods = []
    for Al_pos in Al_positions:
        Al_coods.append(Al_pos.coods())
    Al_coods = [list(arr) for arr in Al_coods]
    assert len(Al_positions) == 16
    assert [0.625, 0.625, 0.625] in Al_coods    
    assert [0.625, 0.625, 0.625] in Al_coods
    assert [0.375, 0.875, 0.125] in Al_coods
    assert [0.875, 0.125, 0.375] in Al_coods
    assert [0.125, 0.375, 0.875] in Al_coods
    assert [0.875, 0.375, 0.125] in Al_coods
    assert [0.375, 0.125, 0.875] in Al_coods
    assert [0.125, 0.875, 0.375] in Al_coods
    assert [0.625, 0.125, 0.125] in Al_coods
    assert [0.375, 0.375, 0.625] in Al_coods
    assert [0.875, 0.625, 0.875] in Al_coods
    assert [0.875, 0.875, 0.625] in Al_coods
    assert [0.375, 0.625, 0.375] in Al_coods
    assert [0.125, 0.625, 0.125] in Al_coods
    assert [0.625, 0.375, 0.375] in Al_coods
    assert [0.625, 0.875, 0.875] in Al_coods
    assert [0.125, 0.125, 0.625] in Al_coods

    O_pos_gen = GeneralPositionsGenerator(O_atom, sym_ops)
    O_positions = O_pos_gen.generate()
    O_coods = []
    for O_pos in O_positions:
        O_coods.append(O_pos.coods())
    O_coods = [list(arr) for arr in O_coods]
    for tup in O_coods:
        tup[0] = round(tup[0], 4)
        tup[1] = round(tup[1], 4)
        tup[2] = round(tup[2], 4)
    print(O_coods)
    assert len(O_positions) == 32
    assert [0.3855, 0.3855, 0.3855] in O_coods
    assert [0.6145, 0.1145, 0.8855] in O_coods
    assert [0.1145, 0.8855, 0.6145] in O_coods
    assert [0.8855, 0.6145, 0.1145] in O_coods
    assert [0.1355, 0.6355, 0.3645] in O_coods
    assert [0.8645, 0.8645, 0.8645] in O_coods
    assert [0.6355, 0.3645, 0.1355] in O_coods
    assert [0.3645, 0.1355, 0.6355] in O_coods
    assert [0.6355, 0.1355, 0.3645] in O_coods
    assert [0.1355, 0.3645, 0.6355] in O_coods  
    assert [0.3645, 0.6355, 0.1355] in O_coods
    assert [0.1145, 0.6145, 0.8855] in O_coods
    assert [0.6145, 0.8855, 0.1145] in O_coods
    assert [0.8855, 0.1145, 0.6145] in O_coods
    assert [0.3855, 0.8855, 0.8855] in O_coods
    assert [0.6145, 0.6145, 0.3855] in O_coods
    assert [0.1145, 0.3855, 0.1145] in O_coods
    assert [0.1355, 0.1355, 0.8645] in O_coods
    assert [0.8645, 0.3645, 0.3645] in O_coods
    assert [0.6355, 0.8645, 0.6355] in O_coods
    assert [0.6355, 0.6355, 0.8645] in O_coods
    assert [0.1355, 0.8645, 0.1355] in O_coods
    assert [0.1145, 0.1145, 0.3855] in O_coods
    assert [0.6145, 0.3855, 0.6145] in O_coods
    assert [0.8855, 0.3855, 0.8855] in O_coods
    assert [0.3855, 0.6145, 0.6145] in O_coods
    assert [0.3645, 0.8645, 0.3645] in O_coods
    assert [0.8645, 0.1355, 0.1355] in O_coods
    assert [0.8645, 0.6355, 0.6355] in O_coods
    assert [0.3855, 0.1145, 0.1145] in O_coods
    assert [0.8855, 0.8855, 0.3855] in O_coods
    assert [0.3645, 0.3645, 0.8645] in O_coods



def test_correctly_generate_diamond_atom_positions():
    cif_reader = CifReader("C.cif")
    c_atom = cif_reader.atoms[0]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositionsGenerator(c_atom, sym_ops)
    new_positions = general_positions.generate()
    new_coods_list = []
    for new_pos in new_positions:
        new_coods_list.append(new_pos.coods())
    new_coods_list = [list(arr) for arr in new_coods_list]
    assert len(new_coods_list) == 8
    assert [0.125, 0.125, 0.125] in new_coods_list
    assert [0.375, 0.375, 0.875] in new_coods_list
    assert [0.875, 0.375, 0.375] in new_coods_list
    assert [0.375, 0.875, 0.375] in new_coods_list
    assert [0.125, 0.625, 0.625] in new_coods_list
    assert [0.625, 0.125, 0.625] in new_coods_list
    assert [0.625, 0.625, 0.125] in new_coods_list
    assert [0.875, 0.875, 0.875] in new_coods_list



def test_generate_correct_quartz_atom_positions():
    cif_reader = CifReader("SiO2.cif")

    O_atom = cif_reader.atoms[0]
    Si_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    O_pos_gen = GeneralPositionsGenerator(O_atom, sym_ops)
    O_positions = O_pos_gen.generate()
    O_coods = []
    for O_pos in O_positions:
        O_coods.append(O_pos.coods())
    O_coods = [list(arr) for arr in O_coods]
    assert len(O_positions) == 18
    assert [0.413, 0.271, 0.2172] in O_coods    

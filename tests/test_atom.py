"""test_atom.py"""

import pytest

from crystal_visualizer.atom import Atom


def test_initialize_atom_successfully():
    atom = Atom("Ba", 0.5, 0.5, 0.5)


def test_retrieve_correct_element_properties_from_atom():
    atom = Atom("Ba", 0.5, 0.5, 0.5)
    assert atom.element.symbol == "Ba"
    assert atom.element.atomic_number == 56
    assert atom.element.atomic_radius == 2.53
    assert atom.element.name == "Barium"


def test_can_change_label_successfully():
    atom = Atom("Ba", 0.5, 0.5, 0.5)
    assert atom.label == "Ba"
    atom.label = "Barium"
    assert atom.label == "Barium"


def test_retrieve_position_vector_successfully():
    atom = Atom("Ba", 0.5, 0.25, 0)
    position = atom.position_vector()
    print(position)
    assert position[0] == 0.5
    assert position[1] == 0.25
    assert position[2] == 0

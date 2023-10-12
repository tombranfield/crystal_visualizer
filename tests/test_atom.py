"""test_atom.py"""

import pytest

import numpy as np

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
    generated_position = atom.position_vector()
    expected_position = np.array([0.5, 0.25, 0])
    assert np.array_equal(generated_position, expected_position)


def test_retrieve_individual_coordinates_successfully():
    atom = Atom("Ba", 0.1, 0.2, 0.3)
    assert atom.position.x == 0.1
    assert atom.position.y == 0.2
    assert atom.position.z == 0.3


def test_can_alter_individual_coordinates_successfull():
    atom = Atom("Ba", 0.1, 0.2, 0.3)
    atom.position.x += 0.5
    new_position = atom.position_vector()
    expected_position = np.array([0.6, 0.2, 0.3])
    assert np.array_equal(new_position, expected_position)

"""test_position.py"""

import numpy as np

from crystal_visualizer.position import Position



def test_can_instantiate_position_successfully():
    position = Position(0.5, 0.5, 0.5)


def test_can_retrieve_coods_array_successfully():
    position = Position(0.5, 0.25, 0.5)
    generated_coods = position.coods()
    expected_coods = np.array([0.5, 0.25, 0.5])
    assert np.allclose(generated_coods, expected_coods)


def test_can_test_for_equality_of_two_equal_positions():
    position_1 = Position(0.5, 0.1, 0.3)
    position_2 = Position(0.5, 0.1, 0.3)
    assert position_1 == position_2


def test_can_test_for_inequality_for_different_positions():
    position_1 = Position(0.5, 0.25, 0.25)
    position_2 = Position(0.25, 0, 0)
    assert position_1 != position_2


"""
def test_can_change_position_successfully():
    position = Position(0.25, 0.5, 0.5)
    position.x += 0.5
    assert position.coods == np.array([0.75, 0.5, 0.5])
"""

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

"""
def test_can_change_position_successfully():
    position = Position(0.25, 0.5, 0.5)
    position.x += 0.5
    assert position.coods == np.array([0.75, 0.5, 0.5])
"""

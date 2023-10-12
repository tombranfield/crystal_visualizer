"""test_element.py"""

import pytest

from crystal_visualizer.element import Element



def test_initialize_barium_retrieve_properties_successfully():
    element = Element("Ba")
    assert element.symbol == "Ba"
    assert element.name == "Barium"
    assert element.atomic_number == 56
    assert element.atomic_radius == 2.53


def test_initialize_lowercase_element_initializes_successfully():
    element = Element("ba")
    assert element.symbol == "Ba"


def test_initializing_non_existant_element_gives_error():
    with pytest.raises(ValueError):
        element = Element("XY")
        

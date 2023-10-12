"""test_element.py"""

from crystal_visualizer.element import Element



def test_initialize_barium_retrieve_properties_successfully():
    element = Element("Ba")
    assert element.symbol == "Ba"
    assert element.name == "Barium"
    assert element.atomic_number == 56
    assert element.atomic_radius == 2.53

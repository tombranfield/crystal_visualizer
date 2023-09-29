"""test_lattice_parameters.py"""

import pytest

from crystal_visualizer.lattice_parameters import LatticeParameters


def test_successfully_create_lattice_parameters_class():
    lp = LatticeParameters(1, 1, 1, 90, 90, 90)


def test_invalid_non_numeric_length_raises_exception():
    with pytest.raises(TypeError):
        lp = LatticeParameters("a", 1, 1, 90, 90, 90)


def test_invalid_negative_length_raises_exception():
    with pytest.raises(ValueError):
        lp = LatticeParameters(-1, 1, 1 ,90, 90, 90)


def test_invalid_non_numeric_angle_raises_exception():
    with pytest.raises(TypeError):
        lp = LatticeParameters(1, 1, 1, "a", 90, 90)


def test_invalid_negative_angle_raises_exception():
    with pytest.raises(ValueError):
        lp = LatticeParameters(1, 1, 1, -90, 90, 90)


def test_exception_raised_if_instantiate_with_too_few_parameters():
    with pytest.raises(TypeError):
        lp = LatticeParameters(1, 1, 1, 90, 90)

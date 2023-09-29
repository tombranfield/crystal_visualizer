"""test_lattice_parameters.py"""

import pytest

from crystal_visualizer.lattice_parameters import LatticeParameters


@pytest.fixture
def lattice_parameters():
    lp = LatticeParameters(1, 2, 3, 30, 60, 90)
    return lp

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


def test_retrieve_length_a_successfully(lattice_parameters):
    assert lattice_parameters.length_a == 1


def test_retrieve_length_b_successfully(lattice_parameters):
    assert lattice_parameters.length_b == 2


def test_retrieve_length_c_successfully(lattice_parameters):
    assert lattice_parameters.length_c == 3


def test_retrieve_angle_alpha_successfully(lattice_parameters):
    assert lattice_parameters.angle_alpha == 30


def test_retrieve_angle_beta_successfully(lattice_parameters):
    assert lattice_parameters.angle_beta == 60


def test_retrieve_angle_gamma_successfully(lattice_parameters):
    assert lattice_parameters.angle_gamma == 90


def test_successfully_change_length_a(lattice_parameters):
    lattice_parameters.length_a = 10
    assert lattice_parameters.length_a == 10


def test_successfully_change_length_b(lattice_parameters):
    lattice_parameters.length_b = 20
    assert lattice_parameters.length_b == 20


def test_successfully_change_length_c(lattice_parameters):
    lattice_parameters.length_c = 30
    assert lattice_parameters.length_c == 30


def test_successfully_change_angle_alpha(lattice_parameters):
    lattice_parameters.angle_alpha = 44
    assert lattice_parameters.angle_alpha == 44


def test_successfully_change_angle_beta(lattice_parameters):
    lattice_parameters.angle_beta = 66
    assert lattice_parameters.angle_beta == 66


def test_successfully_change_angle_gamma(lattice_parameters):
    lattice_parameters.angle_gamma = 99
    assert lattice_parameters.angle_gamma == 99



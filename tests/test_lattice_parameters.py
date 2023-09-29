"""test_lattice_parameters.py"""

import pytest

from crystal_visualizer.lattice_parameters import LatticeParameters


def test_pytest_runs_correctly():
    assert 1 == 1


def test_can_create_lattice_parameters_class():
    lp = LatticeParameters(1, 1, 1, 90, 90, 90)

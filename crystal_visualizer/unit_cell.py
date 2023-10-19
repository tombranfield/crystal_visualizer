"""unit_cell.py"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.space_group import SpaceGroup


class UnitCell:
    """
    Unit cell of the crystal.
    """
    def __init__(self, 
                 atoms_list: Atom, 
                 lattice_parameters: LatticeParameters):
        self.atoms = atoms_list
        self.lattice_parameters = LatticeParameters

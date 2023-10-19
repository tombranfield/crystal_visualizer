"""unit_cell.py"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.lattice_parameters import LatticeParameters


class UnitCell:
    """
    Unit cell of the crystal.
    """
    def __init__(self, 
                 atoms_list: Atom, 
                 lattice_parameters: LatticeParameters):
        self.atoms = atoms_list
        self.lattice_parameters = LatticeParameters

    def print_info(self):
        for atom in self.atoms:
            print(atom.symbol, atom.position_vector())
        for lattice_parameter in self.lattice_parameters:
            print(lattice_parameter)

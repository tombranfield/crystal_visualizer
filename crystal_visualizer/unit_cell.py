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
        self.lattice_param = lattice_parameters

    def print_info(self):
        print("\nLattice Information")
        print("-------------------")
        print("a: ", self.lattice_param.length_a, "A")
        print("b: ", self.lattice_param.length_b, "A")
        print("c: ", self.lattice_param.length_c, "A")
        print("alpha: ", self.lattice_param.angle_alpha, "deg")
        print("beta: ", self.lattice_param.angle_beta, "deg")
        print("gamma: ", self.lattice_param.angle_gamma, "deg")

        print("\nAtom Information")
        print("----------------")
        for atom in self.atoms:
            print(atom.symbol, "position =", atom.position_vector(), end=" ")
            print("atomic_radius =", atom.element.atomic_radius, "A")
        

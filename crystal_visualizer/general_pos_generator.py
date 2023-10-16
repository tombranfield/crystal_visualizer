"""general_positions"""


from crystal_visualizer.cif_reader import CifReader


class GeneralPositions:
    """
    Generate a set of general positions given some starting atoms
    and a set of symmetry operations.
    """
    def __init__(self, starting_atoms, symmetry_ops):
        self.starting_atoms = starting_atoms
        self.symmetry_ops = symmetry_ops

    def generate_general_positions(self):
        # Go through each atom
        # For each atom, generate Position vectors using the sym ops
        # Add each new Position vector to a list
        # Eliminate any duplicate Positions
        for atom in self.starting_atoms:
            cur_pos = atom.position_vector()
            print(cur_pos)



if __name__ == "__main__":
    cif_reader = CifReader("Cu.cif")
    """
    for atom in cif_reader.atoms:
        print(atom.symbol)
        print(atom.position_vector())
    print(cif_reader.symmetry_ops.sym_ops)
    """    
    
    atoms = cif_reader.atoms
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositions(atoms, sym_ops)
    general_positions.generate_general_positions()

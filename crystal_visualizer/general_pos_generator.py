"""general_positions"""


from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.position import Position


class GeneralPositions:
    """
    Generate a set of general positions given some starting atoms
    and a set of symmetry operations.
    """
    def __init__(self, starting_atoms, symmetry_ops):
        self.starting_atoms = starting_atoms
        self.symmetry_ops = symmetry_ops

    def generate(self) -> Atom:
        for atom in self.starting_atoms:
            atom_pos = atom.position_vector()
            x, y, z = atom_pos[0], atom_pos[1], atom_pos[2]
            for sym_op in self.symmetry_ops[:1]:
                x_sym_op = sym_op[0]
                y_sym_op = sym_op[1]
                z_sym_op = sym_op[2]
                
                # Now take the sym op string, convert to a position vec
                # So we need to generate new float x,y,z to make new Position
                if "+" in x_sym_op:
                    x_sym_op.split("+")

    def _sym_op_str_to_pos(self, sym_op_str):
        pass

if __name__ == "__main__":
    cif_reader = CifReader("Cu.cif")
    atoms = cif_reader.atoms
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositions(atoms, sym_ops)
    general_positions.generate_general_positions()

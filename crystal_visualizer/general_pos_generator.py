"""general_positions"""


from crystal_visualizer.atom import Atom
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
            new_positions = []
            for sym_op in self.symmetry_ops[:2]:
                x_op, y_op, z_op = sym_op[0], sym_op[1], sym_op[2]
                new_x = self._sym_op_str_to_pos(atom_pos, x_op)
                new_y = self._sym_op_str_to_pos(atom_pos, y_op)
                new_z = self._sym_op_str_to_pos(atom_pos, z_op)
                new_position = Position(new_x, new_y, new_z)
                new_positions.append(new_position)
            self.print_new_pos(new_positions)
            self.remove_duplicate_pos(new_positions)


    def _sym_op_str_to_pos(self, atom_pos, sym_op_str) -> float:
        x, y, z = atom_pos[0], atom_pos[1], atom_pos[2]
        output = 0.0
        # First account for possible constants
        if "+" in sym_op_str:
            pass
            # find the bit with letters in
            # find the part with numbers in, read, and add
        if "x" in sym_op_str:
            output += x
        if "y" in sym_op_str:
            output += y
        if "z" in sym_op_str:
            output += z
        return output

    
    def print_new_pos(self, new_pos_array):
        for new_pos in new_pos_array:
            print(new_pos.coods())

    def remove_duplicate_pos(self, new_pos_array):
        pass


if __name__ == "__main__":
    cif_reader = CifReader("Cu.cif")
    atoms = cif_reader.atoms
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositions(atoms, sym_ops)
    general_positions.generate()

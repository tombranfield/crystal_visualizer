"""general_positions"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.position import Position
from crystal_visualizer.space_group_symmetry_ops import SpaceGroupSymOps


class GeneralPositionGenerator:
    """
    Generate a set of general positions given some starting atoms
    and a set of symmetry operations.

    In:
        atom: a 

    """
    def __init__(self, atom: Atom, symmetry_ops: SpaceGroupSymOps):
        self.atom = atom
        self.symmetry_ops = symmetry_ops

    def generate(self) -> Atom:
        """
        Output
        """
        orig_atom_pos = self.atom.position_vector()
        print("orig pos:", orig_atom_pos)
        atom_positions = []
        # TODO
        # Adjust slicing to choose different parts
        for sym_op in self.symmetry_ops[:10]:
            # Grab the symmetry op from the string. This works
            x_op, y_op, z_op = sym_op[0], sym_op[1], sym_op[2]

            # Grab the new cood for each of x,y,z using the
            # parsing method. This needs fixing
            new_x = self._sym_op_str_to_pos(orig_atom_pos, x_op)
            new_y = self._sym_op_str_to_pos(orig_atom_pos, y_op)
            new_z = self._sym_op_str_to_pos(orig_atom_pos, z_op)
            
            new_position = Position(new_x, new_y, new_z)
            # TODO eliminate positions outside unit cell
#            if (self._is_pos_in_unit_cell(new_position)
            print(sym_op, end=" ")
            print(new_position.coods())

            if new_position not in atom_positions:
                atom_positions.append(new_position)
#        self.print_new_pos(atom_positions)

    # TODO this doesn't work - need to parse correctly
    def _sym_op_str_to_pos(self, orig_atom_pos, sym_op_str) -> float:
        # TODO read negative numbers
        # TODO read negative numbers with fractions
        x, y, z = orig_atom_pos[0], orig_atom_pos[1], orig_atom_pos[2]
        output = 0.0

        # Handle fraction included
        if "/" in sym_op_str:
            op_parts = sym_op_str.split("+")
            for op_part in op_parts:
                if "/" in op_part:
                    output += self._fraction_str_to_float(op_part)
                else:
                    sym_op_str = op_part

        if "x" in sym_op_str: output += x
        if "y" in sym_op_str: output += y
        if "z" in sym_op_str: output += z
        if "-x" in sym_op_str: output -= 2 * x
        if "-y" in sym_op_str: output -= 2 * y
        if "-z" in sym_op_str: output -= 2 * z
        return output


    def _fraction_str_to_float(self, fraction_str):
        try:
            return float(fraction_str)
        except ValueError:
            nom, denom = fraction_str.split("/")
            return float(nom) / float(denom)

    def _is_pos_in_unit_cell(self, position):
        if (position.x >= 1.0 or
            position.y >= 1.0 or
            position.z >= 1.0):
            return False
        return True

    
    def print_new_pos(self, new_pos_array):
        for new_pos in new_pos_array:
            print(new_pos.coods())
        print(len(new_pos_array))


    def remove_duplicate_pos(self, new_pos_array):
        pass


if __name__ == "__main__":
    """
    # Copper test
    cif_reader = CifReader("Cu.cif")
    atom = cif_reader.atoms[0]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    general_positions = GeneralPositionGenerator(atom, sym_ops)
    general_positions.generate()
    """
    


    # NaCl test
    cif_reader = CifReader("NaCl.cif")
    na_atom = cif_reader.atoms[0]
    cl_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

#    print("Na:")
    na_general_positions = GeneralPositionGenerator(na_atom, sym_ops)
#    na_general_positions.generate()
    print("Cl:")
    cl_general_positions = GeneralPositionGenerator(cl_atom, sym_ops)
    cl_general_positions.generate()

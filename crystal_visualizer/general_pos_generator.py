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
        atom_positions = []
        # TODO
        # count = 1
        for sym_op in self.symmetry_ops:
            x_op, y_op, z_op = sym_op[0], sym_op[1], sym_op[2]

            # Grab the new cood for each of x,y,z using the
            # parsing method. This needs fixing
            new_x = self._sym_op_str_to_pos(orig_atom_pos, x_op)
            new_y = self._sym_op_str_to_pos(orig_atom_pos, y_op)
            new_z = self._sym_op_str_to_pos(orig_atom_pos, z_op)
            
            new_pos = Position(new_x, new_y, new_z)
            #print(count, end=" ")
            count += 1
            #print(sym_op, end=" ")
            #print(new_pos.coods())
            #print()
            if (self._is_pos_in_unit_cell(new_pos)
                and new_pos not in atom_positions):
                atom_positions.append(new_pos)

            # For the generated position, make new positions by
            # translation
            # This is necessary to handle generated values which
            # are outside unit cell when generated using the space group 
            # operations, but are inside the unit cell when translated
            trans_new_pos = []
            trans_new_pos.append(Position(new_pos.x, new_pos.y, new_pos.z))
            trans_new_pos.append(Position(new_pos.x+1, new_pos.y, new_pos.z))
            trans_new_pos.append(Position(new_pos.x, new_pos.y+1, new_pos.z))
            trans_new_pos.append(Position(new_pos.x, new_pos.y, new_pos.z+1))
            trans_new_pos.append(Position(new_pos.x+1, new_pos.y+1, new_pos.z))
            trans_new_pos.append(Position(new_pos.x, new_pos.y+1, new_pos.z+1))
            trans_new_pos.append(Position(new_pos.x+1, new_pos.y, new_pos.z+1))
            trans_new_pos.append(Position(new_pos.x+1, new_pos.y+1, new_pos.z+1))
            for trans_pos in trans_new_pos:
                if (self._is_pos_in_unit_cell(trans_pos)
                and trans_pos not in atom_positions):
                    atom_positions.append(new_pos)


        # Add edge atoms
        # TODO there is probably a cleaner way to do this
        # But let's generate the correct positions first, then clean
        edge_positions = []
        for pos in atom_positions:
            if pos.x == pos.y == pos.z == 0.0:
                edge_positions.append(Position(0.0, 0.0, 1.0))
                edge_positions.append(Position(0.0, 1.0, 0.0))
                edge_positions.append(Position(0.0, 1.0, 1.0))
                edge_positions.append(Position(1.0, 0.0, 0.0))
                edge_positions.append(Position(1.0, 0.0, 1.0))
                edge_positions.append(Position(1.0, 1.0, 0.0))
                edge_positions.append(Position(1.0, 1.0, 1.0))
            if pos.x == 0.0:
                edge_positions.append(Position(1.0, pos.y, pos.z))
            if pos.y == 0.0:
                edge_positions.append(Position(pos.x, 1.0, pos.z))
            if pos.z == 0.0:
                edge_positions.append(Position(pos.x, pos.y, 1.0))
        for edge_pos in edge_positions:
            if edge_pos not in atom_positions:
                atom_positions.append(edge_pos)

        self.print_new_pos(atom_positions)

    def _sym_op_str_to_pos(self, orig_atom_pos, sym_op_str) -> float:
        x, y, z = orig_atom_pos[0], orig_atom_pos[1], orig_atom_pos[2]
        output = 0.0
        if "/" in sym_op_str:
            slash_index = sym_op_str.find("/")
            fraction = sym_op_str[slash_index-1:slash_index+2]
            output += self._fraction_str_to_float(fraction)
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
        if (position.x < 0 or position.x > 1.0 or
            position.y < 0 or position.y > 1.0 or
            position.z < 0 or position.z > 1.0):
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
    print("Cu")
    general_positions = GeneralPositionGenerator(atom, sym_ops)
    general_positions.generate()

    # NaCl test
    cif_reader = CifReader("NaCl.cif")
    na_atom = cif_reader.atoms[0]
    cl_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    print("Na:")
    na_general_positions = GeneralPositionGenerator(na_atom, sym_ops)
    na_general_positions.generate()
    print("Cl:")
    cl_general_positions = GeneralPositionGenerator(cl_atom, sym_ops)
    cl_general_positions.generate()


    """
    # CaF2 test
    cif_reader = CifReader("CaF2.cif")
    ca_atom = cif_reader.atoms[0]
    f_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops
    #print("Ca:")
    #ca_general_positions = GeneralPositionGenerator(ca_atom, sym_ops)
    #ca_general_positions.generate()
    print("F:")
    f_general_positions = GeneralPositionGenerator(f_atom, sym_ops)
    f_general_positions.generate()


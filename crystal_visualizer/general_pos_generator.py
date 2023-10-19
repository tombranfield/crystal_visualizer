"""general_positions"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.position import Position
from crystal_visualizer.space_group_symmetry_ops import SpaceGroupSymOps


class GeneralPositionsGenerator:
    """
    Generate a set of general positions given some starting atoms
    and a set of symmetry operations.

    In:
        atom: a 

    """
    def __init__(self, atom: Atom, symmetry_ops: SpaceGroupSymOps):
        self.atom = atom
        self.symmetry_ops = symmetry_ops

    def generate(self) -> Position:
        """
        Output
        """
        orig_atom_pos = self.atom.position_vector()
        atom_positions = []
        # TODO
        count = 1
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
            #print(sym_op)
            if new_pos.x < 0: new_pos.x += 1
            if new_pos.x > 1: new_pos.x -= 1
            if new_pos.y < 0: new_pos.y += 1
            if new_pos.y > 1: new_pos.y -= 1
            if new_pos.z < 0: new_pos.z += 1
            if new_pos.z > 1: new_pos.z -= 1

            # Round results 
            new_pos.x = round(new_pos.x, 3)
            new_pos.y = round(new_pos.y, 3)
            new_pos.z = round(new_pos.z, 3)

            #print(new_pos.coods())


            if (self._is_pos_in_unit_cell(new_pos)
                and new_pos not in atom_positions):
                atom_positions.append(new_pos)

            # For the generated position, make new positions by
            # translation
            # This is necessary to handle generated values which
            # are outside unit cell when generated using the space group 
            # operations, but are inside the unit cell when translated            

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
            if pos.x == pos.y == 0.0:
                edge_positions.append(Position(1.0, 1.0, pos.z))
            if pos.x == pos.z == 0.0:
                edge_positions.append(Position(1.0, pos.y, 1.0))
            if pos.y == pos.z == 0.0:
                edge_positions.append(Position(pos.x, 1.0, 1.0))
            if pos.x == 0.0:
                edge_positions.append(Position(1.0, pos.y, pos.z))
            if pos.y == 0.0:
                edge_positions.append(Position(pos.x, 1.0, pos.z))
            if pos.z == 0.0:
                edge_positions.append(Position(pos.x, pos.y, 1.0))
        for edge_pos in edge_positions:
            if edge_pos not in atom_positions:
                #TODO
                print("Added", edge_pos.x, edge_pos.y, edge_pos.z)
                atom_positions.append(edge_pos)

        # self.print_new_pos(atom_positions)
        return atom_positions

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

    cif_reader = CifReader("SiO2.cif")

    O_atom = cif_reader.atoms[0]
    Si_atom = cif_reader.atoms[1]
    sym_ops = cif_reader.symmetry_ops.sym_ops

    print("\nSi")
    Si_pos_gen = GeneralPositionsGenerator(Si_atom, sym_ops)
    Si_positions = Si_pos_gen.generate()
    for Si_pos in Si_positions:
        print(Si_pos.coods())
    print(len(Si_positions), "(expected: 6)")

    print("\nO")
    O_pos_gen = GeneralPositionsGenerator(O_atom, sym_ops)
    O_positions = O_pos_gen.generate()
    for O_pos in O_positions:
        print(O_pos.coods())
    print(len(O_positions), "(expected: 6)")

"""general_positions"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.position import Position
from crystal_visualizer.space_group_symmetry_ops import SpaceGroupSymOps


class GeneralPositionsGenerator:
    """
    Generate a set of general positions given an atom 
    and a set of symmetry operations.

    In:
        atom: a 

    """
    def __init__(self, atom: Atom, symmetry_ops: SpaceGroupSymOps):
        self.atom = atom
        self.symmetry_ops = symmetry_ops

    def generate_positions(self) -> Position:
        """
        Output
        """
        orig_pos = self.atom.position_vector()
        atom_positions = []
        for sym_op in self.symmetry_ops:
            new_pos = self._generate_new_pos(orig_pos, sym_op)
            new_pos = self._translate_pos_into_unit_cell(new_pos)
            new_pos = self._round_position(new_pos, 4)
            if (self._is_pos_in_unit_cell(new_pos)
                and not self._is_pos_already_generated(new_pos, atom_positions)):
                atom_positions.append(new_pos)
        self._generate_edge_pos(atom_positions)
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


    def _generate_new_pos(self, orig_pos, sym_op):
        x_op, y_op, z_op = sym_op[0], sym_op[1], sym_op[2]
        new_x = self._sym_op_str_to_pos(orig_pos, x_op)
        new_y = self._sym_op_str_to_pos(orig_pos, y_op)
        new_z = self._sym_op_str_to_pos(orig_pos, z_op)
        new_pos = Position(new_x, new_y, new_z)
        return new_pos


    def _translate_pos_into_unit_cell(self, position):
        new_pos = position
        if new_pos.x < 0: new_pos.x += 1
        if new_pos.x > 1: new_pos.x -= 1
        if new_pos.y < 0: new_pos.y += 1
        if new_pos.y > 1: new_pos.y -= 1
        if new_pos.z < 0: new_pos.z += 1
        if new_pos.z > 1: new_pos.z -= 1
        return new_pos


    def _round_position(self, position, num_dp):
        new_x = round(position.x, num_dp)
        new_y = round(position.y, num_dp)
        new_z = round(position.z, num_dp)
        return Position(new_x, new_y, new_z)


    def _is_pos_in_unit_cell(self, position):
        if (position.x < 0 or position.x > 1.0 or
            position.y < 0 or position.y > 1.0 or
            position.z < 0 or position.z > 1.0):
            return False
        return True


    def _is_pos_already_generated(self, new_pos, atom_positions):
        tol = 0.0001
        for existing_atom in atom_positions:
            if (
                abs(existing_atom.x - new_pos.x) <= tol and
                abs(existing_atom.y - new_pos.y) <= tol and
                abs(existing_atom.z - new_pos.z) <= tol
            ):
                return True
        return False


    def _generate_edge_pos(self, atom_positions):
        #TODO simplify
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
                atom_positions.append(edge_pos)


    
    def print_new_pos(self, new_pos_array):
        for new_pos in new_pos_array:
            print(new_pos.coods())
        print(len(new_pos_array))


if __name__ == "__main__":


    cif_reader = CifReader("YBa2Cu3O7-x.cif")
    Y_atom = cif_reader.atoms[0]
    Ba_atom = cif_reader.atoms[1]
    Cu_atom_1 = cif_reader.atoms[2]
    Cu_atom_2 = cif_reader.atoms[3]
    O_atom = cif_reader.atoms[4]
    O_atom = cif_reader.atoms[5]
    O_atom = cif_reader.atoms[6]
    O_atom = cif_reader.atoms[7]
    sym_ops = cif_reader.symmetry_ops.sym_ops


    for atom in cif_reader.atoms:
        print(atom.symbol)
        print(atom.position_vector())

    print("\nCu 1")
    pos_gen = GeneralPositionsGenerator(Cu_atom_1, sym_ops)
    positions = pos_gen.generate_positions()
    for pos in positions:
        print(pos.coods())
    print(len(positions))

    print("\nCu 2")
    pos_gen = GeneralPositionsGenerator(Cu_atom_2, sym_ops)
    positions = pos_gen.generate_positions()
    for pos in positions:
        print(pos.coods())
    print(len(positions))

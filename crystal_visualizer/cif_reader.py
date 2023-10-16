"""
The crystallographic information file (CIF) is the standard archival format
for storing the information of crystal structures.

For more information about CIF files, please see:
https://www.icur.org/resources/cif/spec/version1.1/cifsyntax
"""

from pathlib import Path
import re

from crystal_visualizer.atom import Atom
from crystal_visualizer.lattice_parameters import LatticeParameters
from crystal_visualizer.space_group_symmetry_ops import SpaceGroupSymOps


class CifReader:
    """
    A class that reads CIF files
    """
    PATH = str(Path(__file__).parents[0] / "data" / "cif_files")

    def __init__(self, filename: str, cif_folder=PATH):
        """Initialize the Cif reader"""
        self.file_path = self.PATH + "/" + filename
        self.lattice_parameters = self.__get_lattice_parameters()
        self.atoms = self.__get_atoms()
        self.symmetry_ops = self.__get_symmetry_ops()

    
    def __get_symmetry_ops(self) -> SpaceGroupSymOps:
        symmetry_ops = SpaceGroupSymOps()
        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            is_reading = False
            for line in lines:
                line = line.rstrip().split()

                # Handle reading the symmetry ops block
                if is_reading:
                    if not line or line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        return symmetry_ops
                    if len(line) > 1:
                        sym_ops_string = line[1]
                    else:
                        sym_ops_string = line[0]
                    line = sym_ops_string.split(",")
                    for index, element in enumerate(line):
                        if element[0] == "+":
                            line[index] = element[1:]
                    symmetry_ops.add_sym_op(line)

                # Need this line so don't get indexing error below
                if not line: continue

                # Check for the start of the symmetry ops block
                if line[0] in ["_symmetry_equiv_pos_as_xyz",
                               "_space_group_symop_operation_xyz"]:
                    is_reading = True


    def __get_lattice_parameters(self) -> LatticeParameters:
        """Gets the lattice parameters from the cif file"""
        len_a, len_b, len_c = 0., 0., 0.
        angle_alpha, angle_beta, angle_gamma = 0., 0., 0.

        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if not line: continue
                # Below could be refactored, but this way is simplier :)
                if line[0] == "_cell_length_a":
                    len_a = self.__float_from_string_with_brackets(line[1])
                if line[0] == "_cell_length_b":
                    len_b = self.__float_from_string_with_brackets(line[1])
                if line[0] == "_cell_length_c":
                    len_c = self.__float_from_string_with_brackets(line[1])
                if line[0] == "_cell_angle_alpha":
                    angle_alpha = self.__float_from_string_with_brackets(line[1])
                if line[0] == "_cell_angle_beta":
                    angle_beta = self.__float_from_string_with_brackets(line[1])
                if line[0] == "_cell_angle_gamma":
                    angle_gamma = self.__float_from_string_with_brackets(line[1])

        return LatticeParameters(
            len_a, len_b, len_c, angle_alpha, angle_beta, angle_gamma)


    def __get_atoms(self) -> Atom:
        atoms = []
        atom_site_type = self._get_atom_site_type()
        is_reading = False
        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.strip().split()
                if not line: continue
                if line[0] == "_" + atom_site_type:
                    is_reading = True
                    continue
                if is_reading:
                    if line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        is_reading = False
                        continue
                    atom = self._read_line_of_atom_data(line, atom_site_type)
                    atoms.append(atom)
            return atoms


    def _set_all_atom_site_types_to_false(self, atom_site_types):
        for atom_site_type in atom_site_types:
            atom_site_types[atom_site_type] = False


    def _check_line_for_atom_site_type(self, atom_site_types, line_str):
        for atom_site_type in atom_site_types.keys():
            if line_str == "_" + atom_site_type:
                self._set_all_atom_site_types_to_false(atom_site_types)
                atom_site_types[atom_site_type] = True


    def _get_atom_site_type(self):
        """Returns the type of atom site used in the cif file"""
        atom_site_types = {
            "atom_site_symmetry_multiplicity": False,
            "atom_site_refinement_flags_occupancy": False,
            "atom_site_calc_flag": False,
            "atom_site_U_iso_or_equiv": False,
        }
        
        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if not line: continue
                self._check_line_for_atom_site_type(atom_site_types, line[0])
        
        for atom_site_type in atom_site_types:
            if atom_site_types[atom_site_type]:
                return atom_site_type


    def _read_line_of_atom_data(self, line, atom_site_type) -> Atom:
        if atom_site_type == "atom_site_calc_flag":
            return self._read_line_atom_site_calc_flag(line)
        if atom_site_type == "atom_site_symmetry_multiplicity":
            return self._read_line_atom_site_symmetry_multiplicity(line)
        if atom_site_type == "atom_site_refinement_flags_occupancy":
            return self._read_line_atom_site_refinement_flags_occupancy(line)
        if atom_site_type == "atom_site_U_iso_or_equiv":
            return self._read_line_atom_site_U_iso_or_equiv(line)


    def _read_line_atom_site_calc_flag(self, line) -> Atom:
        element_symbol = line[0]
        first_digit_match = re.search(r"\d+", element_symbol)
        if first_digit_match:
            element_symbol = element_symbol[:first_digit_match.start()]
            element_symbol = element_symbol.title()
        x = self.__float_from_string_with_brackets(line[-6])
        y = self.__float_from_string_with_brackets(line[-5])
        z = self.__float_from_string_with_brackets(line[-4])
        atom = Atom(element_symbol, x, y, z)
        return atom


    def _read_line_atom_site_symmetry_multiplicity(self, line) -> Atom:
        element_symbol = line[0]
        first_digit_match = re.search(r"\d+", element_symbol)
        if first_digit_match:
            element_symbol = element_symbol[:first_digit_match.start()]
            element_symbol = element_symbol.title()
        x = self.__float_from_string_with_brackets(line[1])
        y = self.__float_from_string_with_brackets(line[2])
        z = self.__float_from_string_with_brackets(line[3])
        atom = Atom(element_symbol, x, y, z)
        return atom


    def _read_line_atom_site_U_iso_or_equiv(self, line) -> Atom:
        element_symbol = line[0]
        first_digit_match = re.search(r"\d+", element_symbol)
        if first_digit_match:
            element_symbol = element_symbol[:first_digit_match.start()]
            element_symbol = element_symbol.title()
            element_symbol = element_symbol.title()
        x = self.__float_from_string_with_brackets(line[-5])
        y = self.__float_from_string_with_brackets(line[-4])
        z = self.__float_from_string_with_brackets(line[-3])
        atom = Atom(element_symbol, x, y, z)
        return atom


    def _read_line_atom_site_refinement_flags_occupancy(self, line) -> Atom:
        element_symbol = line[1]
        x = self.__float_from_string_with_brackets(line[2])
        y = self.__float_from_string_with_brackets(line[3])
        z = self.__float_from_string_with_brackets(line[4])
        atom = Atom(element_symbol, x, y, z)
        return atom


    def __float_from_string_with_brackets(self, number_string):
        """
        Some lattice parameters in cif files contain the error in brackets. This
        function returns a string without these ending brackets.
        """    
        starting_bracket_index = number_string.find("(")
        if starting_bracket_index != -1:        
            return float(number_string[:starting_bracket_index])
        return float(number_string)



if __name__ == "__main__":
    cif_reader = CifReader("Cu.cif")
    print(cif_reader._get_atom_site_type())
    for sym_op in cif_reader.symmetry_ops.sym_ops:
        print(sym_op)
    print(len(cif_reader.symmetry_ops))

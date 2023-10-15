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

    def __get_lattice_parameters(self) -> LatticeParameters:
        """Gets the lattice parameters from the cif file"""
        len_a, len_b, len_c = 0., 0., 0.
        angle_alpha, angle_beta, angle_gamma = 0., 0., 0.

        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if not line: continue
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


    def _get_atom_site_type(self):
        """Returns the type of atom site used in the cif file"""

        atom_site_types = {
            "atom_site_symmetry_multiplicity": False,
            "atom_site_refinement_flags_occupancy": False,
            "atom_site_calc_flag": False,
            "atom_site_U_iso_or_equiv": False,
        }

        def set_all_atom_site_types_to_false():
            for atom_site_type in atom_site_types:
                atom_site_types[atom_site_type] = False

        def check_line_for_atom_site_type(line_str):
            for atom_site_type in atom_site_types.keys():
                if line_str == "_" + atom_site_type:
                    set_all_atom_site_types_to_false()
                    atom_site_types[atom_site_type] = True

        # Read the file and look for the atom site type lines
        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if not line: continue
                check_line_for_atom_site_type(line[0])

        # Return the atom site type
        for atom_site_type in atom_site_types:
            if atom_site_types[atom_site_type]:
                return atom_site_type


    def __get_atoms(self) -> Atom:
        """Gets a list of Atoms from the cif file"""
        atoms = []
        # Reading file twice for atoms and lattice parameters for clarity
        # and testability
        with open(self.file_path, "r") as file_obj:

            # TODO incorporate above atom_site_type here
            atom_site_type = self._get_atom_site_type()

            # TODO
            # if atom_site_type == atom_site_calc_flag:


            # First find the atom site type
            # Write function that returns atom site type
            # Then function that accepts the type, and forwards it
            # to another relevant function that does the processing
            is_atom_site_symmetry_multiplicity = False
            is_atom_site_refinement_flags_occupancy = False
            is_atom_site_calc_flag = False
            is_atom_site_U_iso_or_equiv = False


            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if not line: continue
                if line[0] == "_atom_site_symmetry_multiplicity":
                    is_atom_site_refinement_flags_occupancy = False
                    is_atom_site_calc_flag = False
                    is_atom_site_U_iso_or_equiv = False
                    is_atom_site_symmetry_multiplicity = True
                    continue
                if line[0] == "_atom_site_refinement_flags_occupancy":
                    is_atom_site_symmetry_multiplicity = False
                    is_atom_site_calc_flag = False
                    is_atom_site_U_iso_or_equiv = False
                    is_atom_site_refinement_flags_occupancy = True
                    continue
                if line[0] == "_atom_site_calc_flag":
                    is_atom_site_symmetry_multiplicity = False
                    is_atom_site_refinement_flags_occupancy = False
                    is_atom_site_U_iso_or_equiv = False
                    is_atom_site_calc_flag = True
                    continue
                if line[0] == "_atom_site_U_iso_or_equiv":
                    is_atom_site_symmetry_multiplicity = False
                    is_atom_site_refinement_flags_occupancy = False
                    is_atom_site_calc_flag = False
                    is_atom_site_U_iso_or_equiv = True
                    continue



                if is_atom_site_symmetry_multiplicity:
                    if line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        is_atom_site_symmetry_multiplicity = False
                        continue
                    element_symbol = line[0]
                    first_digit_match = re.search(r"\d+", element_symbol)
                    if first_digit_match:
                        element_symbol = element_symbol[:first_digit_match.start()]
                    element_symbol = element_symbol.title()
                    x = self.__float_from_string_with_brackets(line[1])
                    y = self.__float_from_string_with_brackets(line[2])
                    z = self.__float_from_string_with_brackets(line[3])

                    atom = Atom(element_symbol, x, y, z)
                    atoms.append(atom)

                if is_atom_site_refinement_flags_occupancy:
                    if line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        is_atom_site_refinement_flags_occupancy = False
                        continue
                    element_symbol = line[1]
                    x = self.__float_from_string_with_brackets(line[2])
                    y = self.__float_from_string_with_brackets(line[3])
                    z = self.__float_from_string_with_brackets(line[4])
                    atom = Atom(element_symbol, x, y, z)
                    atoms.append(atom)

                if is_atom_site_calc_flag:
                    if line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        is_atom_site_calc_flag = False
                        continue
                    element_symbol = line[0]
                    first_digit_match = re.search(r"\d+", element_symbol)
                    if first_digit_match:
                        element_symbol = element_symbol[:first_digit_match.start()]
                    element_symbol = element_symbol.title()
                    x = self.__float_from_string_with_brackets(line[-6])
                    y = self.__float_from_string_with_brackets(line[-5])
                    z = self.__float_from_string_with_brackets(line[-4])
                    

                    atom = Atom(element_symbol, x, y, z)
                    atoms.append(atom)

                if is_atom_site_U_iso_or_equiv:
                    if line[0] in ["loop", "loop_"] or line[0][0] == "_":
                        is_atom_site_U_iso_or_equiv = False
                        continue
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
                    atoms.append(atom)


        return atoms

        
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
    filename = "NaCl.cif"
    my_reader = CifReader(filename)

    print(my_reader.lattice_parameters.length_a)
    print(my_reader.lattice_parameters.length_b)
    print(my_reader.lattice_parameters.length_c)
    print(my_reader.lattice_parameters.angle_alpha)
    print(my_reader.lattice_parameters.angle_beta)
    print(my_reader.lattice_parameters.angle_gamma)
    for atom in my_reader.atoms:
        print(atom.symbol)
        print(atom.position_vector())

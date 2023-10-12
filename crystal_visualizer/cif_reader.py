"""
The crystallographic information file (CIF) is the standard archival format
for storing the information of crystal structures.

For more information about CIF files, please see:
https://www.icur.org/resources/cif/spec/version1.1/cifsyntax
or
Hall, S.R., Allen, F.H, Brown, I.D. (1991). The Crystallographic Information
File (CIF): A new standard archive file for Crystallography. Acta Crystallographica
Section A Foundations of Crystallography, 47(6), 655-685.
doi:10.1107/s010876739101067x
"""

from pathlib import Path

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
    
    def __get_lattice_parameters(self) -> LatticeParameters:
        """Gets the lattice parameters from the cif file"""
        len_a, len_b, len_c = 0., 0., 0.
        angle_alpha, angle_beta, angle_gamma = 0., 0., 0.
        with open(self.file_path, "r") as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                line = line.rstrip().split()
                if line[0] == "_cell_length_a":
                    len_a = float(self.__remove_parentheses(line[1]))
                if line[0] == "_cell_length_b":
                    len_b = float(self.__remove_parentheses(line[1]))
                if line[0] == "_cell_length_c":
                    len_c = float(self.__remove_parentheses(line[1]))
                if line[0] == "_cell_angle_alpha":
                    angle_alpha = float(self.__remove_parentheses(line[1]))
                if line[0] == "_cell_angle_beta":
                    angle_beta = float(self.__remove_parentheses(line[1]))
                if line[0] == "_cell_angle_gamma":
                    angle_gamma = float(self.__remove_parentheses(line[1]))
        return LatticeParameters(
            len_a, len_b, len_c, angle_alpha, angle_beta, angle_gamma
        )

    def __remove_parentheses(self, number_string):
        """
        Some lattice paramters in cif files contain the error in brackets. This
        function returns a string without these ending brackets.
        """    
        starting_bracket_index = number_string.find("(")
        if starting_bracket_index != -1:        
            return number_string[:starting_bracket_index]            
        return number_string


    # _cell_length_a
    # _cell_length_b
    # _cell_length_c
    # _cell_angle_alpha
    # _cell_angle_beta
    # _cell_angle_gamma

    # _atom_site_fract_x
    # _atom_site_fract_y

    # _atom_type_oxidation_number
    # _atom_type_radius_bond



if __name__ == "__main__":
    filename = "Cu.cif"
    my_reader = CifReader(filename)

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


class CifReader:
    """
    A module that reads CIF files
    """
    PATH = str(Path(__file__).parents[0] / "data" / "cif_files")

    def __init__(self, filename: str):
        """Initialize the Cif reader"""
        self.file_path = self.PATH + "/" + filename
        print(self.file_path)


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

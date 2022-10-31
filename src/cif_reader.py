"""
The crystallographic information file (CIF) is the standard archival format
for storing the information of crystal structures.

This module contains the CifReader class that takes a CIF file as input,
and saves the information within that CIF file into a CurrentCrystalData
dataclass for use by the rest of the program.

For more information about CIF files, please see:
https://www.icur.org/resources/cif/spec/version1.1/cifsyntax
or
Hall, S.R., Allen, F.H, Brown, I.D. (1991). The Crystallographic Information
File (CIF): A new standard archive file for Crystallography. Acta Crystallographica
Section A Foundations of Crystallography, 47(6), 655-685.
doi:10.1107/s010876739101067x

Note not all the information from the CIF file is read.
For example, experimental apparatus, authors, etc. This module concentrates
on core structural information only of the lattice parameters, and
atom identities and positions.
"""

class CifReader:
    """
    A module that reads CIF files
    """

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
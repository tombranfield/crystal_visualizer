"""cif_to_unit_cell.py"""


from crystal_visualizer.cif_reader import CifReader


class CifToUnitCell:
    """
    Takes a cif and generates a unit cell
    """
    def __init__(self, cif_file):
        self._cif_file = cif_file
        cif_reader = CifReader(self._cif_file)
        cif_atoms = cif_reader.atoms
        symmetry_ops = cif_reader.symmetry_ops

    def generate_atoms(self):

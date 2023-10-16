"""cif_to_unit_cell.py"""


class CifToUnitCell:
    """
    Takes a cif and generates a unit cell
    """
    def __init__(self, cif_file):
        self._cif_file = cif_file

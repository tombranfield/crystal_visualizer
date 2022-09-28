#TODO id number as a class method
#TODO input testing for symbol and fractional coordinates
#TODO testing

"""
This module contains the Atom class which represents a single
atom within the unit cell of the crystal structure.
"""

from element import Element


class Atom:
    """
    A class representing an atom.

    Args:
        in_chemical_symbol: a one or two-letter string corresponding to the
        symbol of a chemical element as represented in the periodic table.
        Elements 1 to 118 can be chosen.
        in_fract_x, in_fract_y, int_fract_z: floating point numbers between 0
        (inclusive) and 1 (exclusive) representing the fractional coordinates
        of the atom within the unit cell.

    Returns:
        an instance of Atom representing a single atom.
    """
    def __init__(self,  in_chemical_symbol: str,
                        in_fract_x: float,
                        in_fract_y: float,
                        in_fract_z: float):
        """
        Initializes the Atom class.

        Note the chemical element of the atom is read-only, but the fractional
        coordinates and label must be able to change.
        """
        self._element = Element(in_chemical_symbol)
        self.label = self._element.symbol
        self.fract_x = in_fract_x
        self.fract_y = in_fract_y
        self.fract_z = in_fract_z

    @property
    def element(self) -> Element:
        """Returns the chemical element of atom."""
        return self._element
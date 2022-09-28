"""
This module contains the Atom class which represents a single
atom within the unit cell of the crystal structure.
"""

from element import Element


class Atom:
    """
    A class representing an atom.
    """
    def __init__(self,  in_chemical_symbol: str,
                        in_fract_x: float,
                        in_fract_y: float,
                        in_fract_z: float):
        """Initializes the Atom class.

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
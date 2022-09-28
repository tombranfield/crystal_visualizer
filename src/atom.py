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
        """Initializes the Atom class."""
        self._element = Element(in_chemical_symbol)
        self._fract_x = in_fract_x
        self._fract_y = in_fract_y
        self._fract_z = in_fract_z
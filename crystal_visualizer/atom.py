"""atom.py"""


import numpy as np

from crystal_visualizer.element import Element
from crystal_visualizer.position import Position

class Atom:
    """
    A class representing an atom.

    Args:
        in_chemical_symbol: a one or two-letter string corresponding to the
        symbol of a chemical element as represented in the periodic table.
        Elements 1 to 118 can be chosen.
        x, y, z: floating point numbers between 0
        (inclusive) and 1 (exclusive) representing the fractional coordinates
        of the atom within the unit cell.

    Returns:
        an instance of Atom representing a single atom.
    """
    def __init__(self,  in_chemical_symbol: str,
                        x: float, 
                        y: float,
                        z: float):
        """Initializes the Atom class."""
        self._element = Element(in_chemical_symbol)
        self.label = self._element.symbol
        self.position = Position(x, y, z)

    @property
    def element(self) -> Element:
        """Returns the chemical element of atom.

        Note this returns an instance of the Element class, and so can be used to
        access the properties of that element if required.
        """
        return self._element

    @property
    def symbol(self):
        """Returns the chemical symbol of the atom"""
        return self._element.symbol

    @property
    def position_vector(self):
        return self.position.coods
    
    @property
    def label(self):
        """Returns the label of the atom"""
        return self._label

    @label.setter
    def label(self, new_label: str):
        """Sets a new label for the atom"""
        max_label_length = 10
        if not isinstance(new_label, str):
            raise TypeError("The label must be a string")
        if len(new_label) > max_label_length:
            raise ValueError(f"The label must be {max_label_length} characters or fewer")
        self._label = new_label

    def __verify_coordinate(self, in_fract_cood: float):
        """Verifies that a given fractional coordinate is valid.

        Raises an error if invalid, otherwise does nothing.
        """
        if not isinstance(in_fract_cood, float):
            if in_fract_cood not in [0, 1]:
                raise AttributeError("Fractional coordinates must be floating numbers")
        if in_fract_cood < 0 or in_fract_cood > 1:
            raise ValueError("Fractional coordinates must be in the range [0, 1]")


def main():
    """Main method for this module, used primarily for quick testing"""
    my_atom = Atom("Ba", 0.0, 0.5, 0.5)
    print(my_atom.element)


if __name__ == "__main__":
    main()

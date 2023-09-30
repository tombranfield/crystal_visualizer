#TODO id number as a class method
#TODO input testing for symbol and fractional coordinates
#TODO testing
#TODO put max label length in an external constants file
#TODO add oxidation state
#TODO add atomic radius (set default, able to change)

"""
This module contains the Atom class which represents a single
atom within the unit cell of the crystal structure.
"""

import numpy as np

from crystal_visualizer.element import Element


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
        """Initializes the Atom class."""
        self._element = Element(in_chemical_symbol)
        self.label = self._element.symbol
        self.fract_x = in_fract_x
        self.fract_y = in_fract_y
        self.fract_z = in_fract_z

    @property
    def element(self) -> Element:
        """Returns the chemical element of atom.

        Note this returns an instance of the Element class, and so can be used to
        access the properties of that element if required. For example the molar
        mass or magnetic properties of the element might be included in an expanded
        version of this program."""
        return self._element

    @element.setter
    def element(self, new_element_symbol: str):
        """Sets the new element for the atom.

        Note that changing the element changes the label"""
        #self._element = Element(new_element_symbol)
        #self.label(new_element_symbol)
        # TODO
        pass

    def position(self) -> np.array:
        """Returns the position vector the array"""
        return np.array([self.fract_x, self.fract_y, self.fract_z])
        
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

    @property
    def fract_x(self):
        """Returns the x-axis fractional coordinate"""
        return self._fract_x

    @fract_x.setter
    def fract_x(self, in_fract_x):
        """Verifies and sets the value of the x-axis fractional coordinate"""
        self.__verify_coordinate(in_fract_x)
        self._fract_x = in_fract_x

    @property
    def fract_y(self):
        """Returns the y-axis fractional coordinate"""
        return self._fract_y

    @fract_y.setter
    def fract_y(self, in_fract_y):
        """Verifies and sets the value of the y-axis fractional coordinate"""
        self.__verify_coordinate(in_fract_y)
        self._fract_y = in_fract_y

    @property
    def fract_z(self):
        """Returns the z-axis fractional coordinate"""
        return self._fract_z

    @fract_z.setter
    def fract_z(self, in_fract_z):
        "Verifies and sets the value of the z-axis fractional coordinate"
        self.__verify_coordinate(in_fract_z)
        self._fract_z = in_fract_z

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

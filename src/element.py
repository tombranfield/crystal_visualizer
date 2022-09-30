#TODO add remaining chemical elements to ElementProperties and elements
#TODO add tests for Element class

"""
This module contains the Element class that represents a chemical element
for each atom within a crystal structure.

The user can assign a chemical element using either its symbol, for example
by assigning (for example) atom_element = Element("Ba"). Properties of the
element such as its atomic number or element name can then be retrieved using
atom_element.atomic_number or atom_element.name, for example.
"""

from collections import namedtuple


class Element:
    """A class representing a chemical element.

    An element is chosen to be an instance for the class. Upon initialization,
    the instance will take properties of the chosen element from the
    corresponding named tuple ElementProperties held within the elements
    dictionary, and assign them as read-only attributes.

    Args:
        in_symbol: a string of one or two letters corresponding to the
        chemical symbol of the element from the periodic table. Elements from
        Z=1 to Z=118 can be selected.

    Returns:
        a class instance containing the properties of the chosen element.
    """

    def __init__(self, in_symbol: str):
        """Initialize the element using its chemical symbol """
        in_symbol = in_symbol.title()
        self.__verify_symbol(in_symbol)
        self._symbol = elements[in_symbol].symbol
        self._name = elements[self.symbol].name
        self._atomic_number = elements[self.symbol].atomic_number

    # Note symbol, name, and atomic_number are read-only
    @property
    def symbol(self) -> str:
        """Returns the chemical symbol of the element"""
        return self._symbol

    @property
    def name(self) -> str:
        """Returns the name of the element"""
        return self._name

    @property
    def atomic_number(self) -> int:
        """Returns the atomic number of the element"""
        return self._atomic_number

    # Note we do not use a property setter as symbol must be read-only
    def __verify_symbol(self, chemical_symbol: str):
        """Verifies that a given string represents a valid chemical symbol.

        If successful, no action is taken. Otherwise, an appropriate exception
        is raised.
        """
        if not isinstance(chemical_symbol, str):
            raise TypeError("You must supply the chemical symbol as a string")
        if chemical_symbol.title() not in elements:
            raise ValueError("Not a valid chemical element symbol")


# Put element properties into a named tuple for readability and immutability
# Using namedtuple also allows extra properties (eg molar mass or electronic
# configuration) to be added in the future, if necessary.
# For now, only the symbol, name, and atomic number is necessary.
ElementProperties = namedtuple("Element", ["atomic_number", "symbol", "name"])

elements = {
    # Period 1
    "H": ElementProperties(1, "H", "hydrogen"),
    "He": ElementProperties(2, "He", "helium"),

    # Period 2
    "Li": ElementProperties(3, "Li", "lithium"),
    "Be": ElementProperties(4, "Be", "beryllium"),
    "B": ElementProperties(5, "B", "boron"),
    "C": ElementProperties(6, "C", "carbon"),
    "N": ElementProperties(7, "N", "nitrogen"),
    "O": ElementProperties(8, "O", "oxygen"),
    "F": ElementProperties(9, "F", "fluorine"),
    "Ne": ElementProperties(10, "Ne", "neon"),

    # Period 3
    "Na": ElementProperties(11, "Na", "sodium"),
    "Mg": ElementProperties(12, "Mg", "magnesium"),
    "Al": ElementProperties(13, "Al", "aluminium"),
    "Si": ElementProperties(14, "Si", "silicon"),
    "P": ElementProperties(15, "P", "phosphorus"),
    "S": ElementProperties(16, "S", "sulphur"),
    "Cl": ElementProperties(17, "Cl", "chlorine"),
    "Ar": ElementProperties(18, "Ar", "argon"),

    # Period 4
    "K": ElementProperties(19, "K", "potassium"),
    "Ca": ElementProperties(20, "Ca", "calcium"),
    "Sc": ElementProperties(21, "Sc", "scandium"),
    "Ti": ElementProperties(22, "Ti", "titanium"),
    "V": ElementProperties(23, "V", "vanadium"),
    "Cr": ElementProperties(24, "Cr", "chromium"),
    "Mn": ElementProperties(25, "Mn", "manganese"),
    "Fe": ElementProperties(26, "Fe", "iron"),
    "Co": ElementProperties(27, "Co", "cobalt"),
    "Ni": ElementProperties(28, "Ni", "nickel"),
    "Cu": ElementProperties(29, "Cu", "copper"),
    "Zn": ElementProperties(30, "Zn", "zinc"),
    "Ga": ElementProperties(31, "Ga", "gallium"),
    "Ge": ElementProperties(32, "Ge", "germanium"),
    "As": ElementProperties(33, "As", "arsenic"),
    "Se": ElementProperties(34, "Se", "selenium"),
    "Br": ElementProperties(35, "Br", "bromine"),
    "Kr": ElementProperties(36, "Kr", "krypton"),

    # Period 5
    "Rb": ElementProperties(37, "Rb", "rubidium"),
    "Sr": ElementProperties(38, "Sr", "strontium"),
    "Y": ElementProperties(39, "Y", "yttrium"),
    "Zr": ElementProperties(40, "Zr", "zirconium"),
    "Nb": ElementProperties(41, "Nb", "niobium"),
    "Mo": ElementProperties(42, "Mo", "molybdenum"),
    "Tc": ElementProperties(43, "Tc", "technetium"),
    "Ru": ElementProperties(44, "Ru", "ruthenium"),
    "Rh": ElementProperties(45, "Rh", "rhodium"),
    "Pd": ElementProperties(46, "Pd", "palladium"),
    "Ag": ElementProperties(47, "Ag", "silver"),
    "Cd": ElementProperties(48, "Cd", "cadmium"),
    "In": ElementProperties(49, "In", "indium"),
    "Sn": ElementProperties(50, "Sn", "tin"),
    "Sb": ElementProperties(51, "Sb", "antimony"),
    "Te": ElementProperties(52, "Te", "tellurium"),
    "I": ElementProperties(53, "I", "iodine"),
    "Xe": ElementProperties(54, "Xe", "xenon"),

    # Period 6
    "Cs": ElementProperties(55, "Cs", "caesium"),
    "Ba": ElementProperties(56, "Ba", "barium"),
    "La": ElementProperties(57, "La", "lanthanum"),
    "Ce": ElementProperties(58, "Ce", "cerium"),
    "Pr": ElementProperties(59, "Pr", "praesodymium"),
    "Nd": ElementProperties(60, "Nd", "neodymium"),
    "Pm": ElementProperties(61, "Pm", "promethium"),
    "Sm": ElementProperties(62, "Sm", "samarium"),
    "Eu": ElementProperties(63, "Eu", "europium"),
    "Gd": ElementProperties(64, "Gd", "gadolinium"),
    "Tb": ElementProperties(65, "Tb", "terbium"),
    "Dy": ElementProperties(66, "Dy", "dysprosium"),
    "Ho": ElementProperties(67, "Ho", "holmium"),
    "Er": ElementProperties(68, "Er", "erbium"),
    "Tm": ElementProperties(69, "Tm", "thulium"),
    "Yb": ElementProperties(70, "Yb", "ytterbium"),
    "Lu": ElementProperties(71, "Lu", "lutetium"),
    "Hf": ElementProperties(72, "Hf", "hafnium"),
    "Ta": ElementProperties(73, "Ta", "tantalum"),
    "W": ElementProperties(74, "W", "tungsten"),
    "Re": ElementProperties(75, "Re", "rhenium"),
    "Os": ElementProperties(76, "Os", "osmium"),
    "Ir": ElementProperties(77, "Ir", "iridium"),
    "Pt": ElementProperties(78, "Pt", "platinum"),
    "Au": ElementProperties(79, "Au", "gold"),
    "Hg": ElementProperties(80, "Hg", "mercury"),
    "Tl": ElementProperties(81, "Tl", "thallium"),
    "Pb": ElementProperties(82, "Pb", "lead"),
    "Bi": ElementProperties(83, "Bi", "bismuth"),
    "Po": ElementProperties(84, "Po", "polonium"),
    "At": ElementProperties(85, "At", "astatine"),
    "Rn": ElementProperties(86, "Rn", "radon"),
}


def main():
    """Main function. Here for the purpose of quick tests"""
    my_element = Element("123")
    print(my_element.name)


if __name__ == "__main__":
    main()
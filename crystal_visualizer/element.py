"""element.py"""


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
        self._atomic_radius = elements[self.symbol].atomic_radius

    @property
    def symbol(self) -> str:
        """Returns the chemical symbol of the element"""
        return self._symbol

    @property
    def name(self) -> str:
        """Returns the name of the element"""
        return self._name.title()

    @property
    def atomic_number(self) -> int:
        """Returns the atomic number of the element"""
        return self._atomic_number

    @property
    def atomic_radius(self) -> float:
        """Returns the atomic radius of the element"""
        return self._atomic_radius

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


ElementProperties = namedtuple("Element", ["atomic_number", "symbol", "name", "atomic_radius"])

elements = {
    # Period 1
    "H": ElementProperties(1, "H", "hydrogen", 0.53),
    "He": ElementProperties(2, "He", "helium", 0.31),

    # Period 2
    "Li": ElementProperties(3, "Li", "lithium", 1.67),
    "Be": ElementProperties(4, "Be", "beryllium", 1.12),
    "B": ElementProperties(5, "B", "boron", 0.87),
    "C": ElementProperties(6, "C", "carbon", 0.67),
    "N": ElementProperties(7, "N", "nitrogen", 0.56),
    "O": ElementProperties(8, "O", "oxygen", 0.58),
    "F": ElementProperties(9, "F", "fluorine", 0.42),
    "Ne": ElementProperties(10, "Ne", "neon", 0.38),

    # Period 3
    "Na": ElementProperties(11, "Na", "sodium", 1.90),
    "Mg": ElementProperties(12, "Mg", "magnesium", 1.45),
    "Al": ElementProperties(13, "Al", "aluminium", 1.18),
    "Si": ElementProperties(14, "Si", "silicon", 1.11),
    "P": ElementProperties(15, "P", "phosphorus", 0.98),
    "S": ElementProperties(16, "S", "sulphur", 0.88),
    "Cl": ElementProperties(17, "Cl", "chlorine", 0.79),
    "Ar": ElementProperties(18, "Ar", "argon", 0.71),

    # Period 4
    "K": ElementProperties(19, "K", "potassium", 2.43),
    "Ca": ElementProperties(20, "Ca", "calcium", 1.94),
    "Sc": ElementProperties(21, "Sc", "scandium", 1.84),
    "Ti": ElementProperties(22, "Ti", "titanium", 1.76),
    "V": ElementProperties(23, "V", "vanadium", 1.71),
    "Cr": ElementProperties(24, "Cr", "chromium", 1.66),
    "Mn": ElementProperties(25, "Mn", "manganese", 1.61),
    "Fe": ElementProperties(26, "Fe", "iron", 1.56),
    "Co": ElementProperties(27, "Co", "cobalt", 1.52),
    "Ni": ElementProperties(28, "Ni", "nickel", 1.49),
    "Cu": ElementProperties(29, "Cu", "copper", 1.45),
    "Zn": ElementProperties(30, "Zn", "zinc", 1.42),
    "Ga": ElementProperties(31, "Ga", "gallium", 1.36),
    "Ge": ElementProperties(32, "Ge", "germanium", 1.25),
    "As": ElementProperties(33, "As", "arsenic", 1.14),
    "Se": ElementProperties(34, "Se", "selenium", 1.03),
    "Br": ElementProperties(35, "Br", "bromine", 0.94),
    "Kr": ElementProperties(36, "Kr", "krypton", 0.88),

    # Period 5
    "Rb": ElementProperties(37, "Rb", "rubidium", 2.65),
    "Sr": ElementProperties(38, "Sr", "strontium", 2.19),
    "Y": ElementProperties(39, "Y", "yttrium", 2.12),
    "Zr": ElementProperties(40, "Zr", "zirconium", 2.06),
    "Nb": ElementProperties(41, "Nb", "niobium", 1.98),
    "Mo": ElementProperties(42, "Mo", "molybdenum", 1.90),
    "Tc": ElementProperties(43, "Tc", "technetium", 1.83),
    "Ru": ElementProperties(44, "Ru", "ruthenium", 1.78),
    "Rh": ElementProperties(45, "Rh", "rhodium", 1.73),
    "Pd": ElementProperties(46, "Pd", "palladium", 1.69),
    "Ag": ElementProperties(47, "Ag", "silver", 1.65),
    "Cd": ElementProperties(48, "Cd", "cadmium", 1.61),
    "In": ElementProperties(49, "In", "indium", 1.56),
    "Sn": ElementProperties(50, "Sn", "tin", 1.45),
    "Sb": ElementProperties(51, "Sb", "antimony", 1.33),
    "Te": ElementProperties(52, "Te", "tellurium", 1.23),
    "I": ElementProperties(53, "I", "iodine", 1.15),
    "Xe": ElementProperties(54, "Xe", "xenon", 1.08),

    # Period 6
    "Cs": ElementProperties(55, "Cs", "caesium", 2.98),
    "Ba": ElementProperties(56, "Ba", "barium", 2.53),
    "La": ElementProperties(57, "La", "lanthanum", 1.95),
    "Ce": ElementProperties(58, "Ce", "cerium", 1.85),
    "Pr": ElementProperties(59, "Pr", "praesodymium", 2.47),
    "Nd": ElementProperties(60, "Nd", "neodymium", 2.06),
    "Pm": ElementProperties(61, "Pm", "promethium", 2.05),
    "Sm": ElementProperties(62, "Sm", "samarium", 2.38),
    "Eu": ElementProperties(63, "Eu", "europium", 2.31),
    "Gd": ElementProperties(64, "Gd", "gadolinium", 2.33),
    "Tb": ElementProperties(65, "Tb", "terbium", 2.25),
    "Dy": ElementProperties(66, "Dy", "dysprosium", 2.28),
    "Ho": ElementProperties(67, "Ho", "holmium", 2.26),
    "Er": ElementProperties(68, "Er", "erbium", 2.26),
    "Tm": ElementProperties(69, "Tm", "thulium", 2.22),
    "Yb": ElementProperties(70, "Yb", "ytterbium", 2.22),
    "Lu": ElementProperties(71, "Lu", "lutetium", 2.17),
    "Hf": ElementProperties(72, "Hf", "hafnium", 2.08),
    "Ta": ElementProperties(73, "Ta", "tantalum", 2.00),
    "W": ElementProperties(74, "W", "tungsten", 1.93),
    "Re": ElementProperties(75, "Re", "rhenium", 1.88),
    "Os": ElementProperties(76, "Os", "osmium", 1.85),
    "Ir": ElementProperties(77, "Ir", "iridium", 1.80),
    "Pt": ElementProperties(78, "Pt", "platinum", 1.77),
    "Au": ElementProperties(79, "Au", "gold", 1.74),
    "Hg": ElementProperties(80, "Hg", "mercury", 1.71),
    "Tl": ElementProperties(81, "Tl", "thallium", 1.56),
    "Pb": ElementProperties(82, "Pb", "lead", 1.54),
    "Bi": ElementProperties(83, "Bi", "bismuth", 1.43),
    "Po": ElementProperties(84, "Po", "polonium", 1.35),
    "At": ElementProperties(85, "At", "astatine", 1.27),
    "Rn": ElementProperties(86, "Rn", "radon", 1.20),

    # Period 7
    "Ac": ElementProperties(89, "Ac", "actinum", 1.95),
    "Th": ElementProperties(90, "Th", "thorium", 1.80),
    "Pa": ElementProperties(91, "Pa", "protactinum", 1.80),
    "U": ElementProperties(92, "U", "uranium", 1.75),
    "Np": ElementProperties(93, "Np", "neptunium", 1.75),
    "Pu": ElementProperties(94, "Pu", "plutonium", 1.75),
    "Am": ElementProperties(95, "Am", "americium", 1.75),
}


def main():
    """Main function. Here for the purpose of quick tests"""
    my_element = Element("Ba")
    print(my_element.symbol)
    print(my_element.name)
    print(my_element.atomic_number)
    print(my_element.atomic_radius)


if __name__ == "__main__":
    main()

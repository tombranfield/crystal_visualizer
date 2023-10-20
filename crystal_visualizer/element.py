"""element.py"""


from collections import namedtuple


class Element:
    """A class representing a chemical element.

    An element is chosen to be an instance for the class. Upon initialization,
    the instance will take properties of the chosen element from the
    corresponding named tuple ElementProperties held within the elements
    dictionary below this class, and assign them as read-only attributes.

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
        self._colour = elements[self.symbol].colour

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

    @property
    def colour(self) -> str:
        """Returns the hex colour code of the element"""
        return self._colour

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


ElementProperties = namedtuple("Element", ["atomic_number", "symbol", "name", "atomic_radius", "colour"])

elements = {
    # Period 1
    "H": ElementProperties(1, "H", "hydrogen", 0.53, "#FFCCCC"),
    "He": ElementProperties(2, "He", "helium", 0.31, "#FCE8CE"),

    # Period 2
    "Li": ElementProperties(3, "Li", "lithium", 1.67, "#86E074"),
    "Be": ElementProperties(4, "Be", "beryllium", 1.12, "#5ED77B"),
    "B": ElementProperties(5, "B", "boron", 0.87, "#1FA20F"),
    "C": ElementProperties(6, "C", "carbon", 0.67, "#804929"),
    "N": ElementProperties(7, "N", "nitrogen", 0.56, "#B0B9E6"),
    "O": ElementProperties(8, "O", "oxygen", 0.58, "#FE0300"),
    "F": ElementProperties(9, "F", "fluorine", 0.42, "#B0B9E6"),
    "Ne": ElementProperties(10, "Ne", "neon", 0.38, "#FE37B5"),

    # Period 3
    "Na": ElementProperties(11, "Na", "sodium", 1.90, "#F9DC3C"),
    "Mg": ElementProperties(12, "Mg", "magnesium", 1.45, "#FB7B15"),
    "Al": ElementProperties(13, "Al", "aluminium", 1.18, "#81B2D6"),
    "Si": ElementProperties(14, "Si", "silicon", 1.11, "#1B3BFA"),
    "P": ElementProperties(15, "P", "phosphorus", 0.98, "#C09CC2"),
    "S": ElementProperties(16, "S", "sulphur", 0.88, "#FFFA00"),
    "Cl": ElementProperties(17, "Cl", "chlorine", 0.79, "#31FC02"),
    "Ar": ElementProperties(18, "Ar", "argon", 0.71, "#CFFEC4"),

    # Period 4
    "K": ElementProperties(19, "K", "potassium", 2.43, "#A121F6"),
    "Ca": ElementProperties(20, "Ca", "calcium", 1.94, "#5A96BD"),
    "Sc": ElementProperties(21, "Sc", "scandium", 1.84, "#B563AB"),
    "Ti": ElementProperties(22, "Ti", "titanium", 1.76, "#78CAFF"),
    "V": ElementProperties(23, "V", "vanadium", 1.71, "#E51900"),
    "Cr": ElementProperties(24, "Cr", "chromium", 1.66, "#00009E"),
    "Mn": ElementProperties(25, "Mn", "manganese", 1.61, "#A8089E"),
    "Fe": ElementProperties(26, "Fe", "iron", 1.56, "#B57100"),
    "Co": ElementProperties(27, "Co", "cobalt", 1.52, "#0000AF"),
    "Ni": ElementProperties(28, "Ni", "nickel", 1.49, "#B7BBBD"),
    "Cu": ElementProperties(29, "Cu", "copper", 1.45, "#2247DC"),
    "Zn": ElementProperties(30, "Zn", "zinc", 1.42, "#8F8F81"),
    "Ga": ElementProperties(31, "Ga", "gallium", 1.36, "#9EE373"),
    "Ge": ElementProperties(32, "Ge", "germanium", 1.25, "#7E6EA6"),
    "As": ElementProperties(33, "As", "arsenic", 1.14, "#74D057"),
    "Se": ElementProperties(34, "Se", "selenium", 1.03, "#9AEF0F"),
    "Br": ElementProperties(35, "Br", "bromine", 0.94, "#7E3102"),
    "Kr": ElementProperties(36, "Kr", "krypton", 0.88, "#FAC1F3"),

    # Period 5
    "Rb": ElementProperties(37, "Rb", "rubidium", 2.65, "#FF0099"),
    "Sr": ElementProperties(38, "Sr", "strontium", 2.19, "#00FF26"),
    "Y": ElementProperties(39, "Y", "yttrium", 2.12, "#66988E"),
    "Zr": ElementProperties(40, "Zr", "zirconium", 2.06, "#00FF00"),
    "Nb": ElementProperties(41, "Nb", "niobium", 1.98, "#4CB276"),
    "Mo": ElementProperties(42, "Mo", "molybdenum", 1.90, "#B386AF"),
    "Tc": ElementProperties(43, "Tc", "technetium", 1.83, "#CDAFCA"),
    "Ru": ElementProperties(44, "Ru", "ruthenium", 1.78, "#CFB7AD"),
    "Rh": ElementProperties(45, "Rh", "rhodium", 1.73, "#CDD1AB"),
    "Pd": ElementProperties(46, "Pd", "palladium", 1.69, "#C1C3B8"),
    "Ag": ElementProperties(47, "Ag", "silver", 1.65, "#B7BBBD"),
    "Cd": ElementProperties(48, "Cd", "cadmium", 1.61, "#F21EDC"),
    "In": ElementProperties(49, "In", "indium", 1.56, "#D780BB"),
    "Sn": ElementProperties(50, "Sn", "tin", 1.45, "#9A8EB9"),
    "Sb": ElementProperties(51, "Sb", "antimony", 1.33, "#D7834F"),
    "Te": ElementProperties(52, "Te", "tellurium", 1.23, "#ADA251"),
    "I": ElementProperties(53, "I", "iodine", 1.15, "#8E1F8A"),
    "Xe": ElementProperties(54, "Xe", "xenon", 1.08, "#9AA1F8"),

    # Period 6
    "Cs": ElementProperties(55, "Cs", "caesium", 2.98, "#0EFEB9"),
    "Ba": ElementProperties(56, "Ba", "barium", 2.53, "#1EEF2C"),
    "La": ElementProperties(57, "La", "lanthanum", 1.95, "#5AC449"),
    "Ce": ElementProperties(58, "Ce", "cerium", 1.85, "#D1FC06"),
    "Pr": ElementProperties(59, "Pr", "praesodymium", 2.47, "#FCE105"),
    "Nd": ElementProperties(60, "Nd", "neodymium", 2.06, "#FB8D06"),
    "Pm": ElementProperties(61, "Pm", "promethium", 2.05, "#0000F4"),
    "Sm": ElementProperties(62, "Sm", "samarium", 2.38, "#FC067D"),
    "Eu": ElementProperties(63, "Eu", "europium", 2.31, "#FA07D5"),
    "Gd": ElementProperties(64, "Gd", "gadolinium", 2.33, "#C003FF"),
    "Tb": ElementProperties(65, "Tb", "terbium", 2.25, "#7104FE"),
    "Dy": ElementProperties(66, "Dy", "dysprosium", 2.28, "#3106FC"),
    "Ho": ElementProperties(67, "Ho", "holmium", 2.26, "#0741FB"),
    "Er": ElementProperties(68, "Er", "erbium", 2.26, "#49723A"),
    "Tm": ElementProperties(69, "Tm", "thulium", 2.22, "#0000E0"),
    "Yb": ElementProperties(70, "Yb", "ytterbium", 2.22, "#27FCF4"),
    "Lu": ElementProperties(71, "Lu", "lutetium", 2.17, "#26FDB5"),
    "Hf": ElementProperties(72, "Hf", "hafnium", 2.08, "#B4B359"),
    "Ta": ElementProperties(73, "Ta", "tantalum", 2.00, "#B79A56"),
    "W": ElementProperties(74, "W", "tungsten", 1.93, "#8D8A7F"),
    "Re": ElementProperties(75, "Re", "rhenium", 1.88, "#B3B08E"),
    "Os": ElementProperties(76, "Os", "osmium", 1.85, "#C8B178"),
    "Ir": ElementProperties(77, "Ir", "iridium", 1.80, "#C9CE72"),
    "Pt": ElementProperties(78, "Pt", "platinum", 1.77, "#CBC5BF"),
    "Au": ElementProperties(79, "Au", "gold", 1.74, "#FEB238"),
    "Hg": ElementProperties(80, "Hg", "mercury", 1.71, "#D3B7CB"),
    "Tl": ElementProperties(81, "Tl", "thallium", 1.56, "#95896C"),
    "Pb": ElementProperties(82, "Pb", "lead", 1.54, "#52535B"),
    "Bi": ElementProperties(83, "Bi", "bismuth", 1.43, "#D22FF7"),
    "Po": ElementProperties(84, "Po", "polonium", 1.35, "#0000FF"),
    "At": ElementProperties(85, "At", "astatine", 1.27, "#0000FF"),
    "Rn": ElementProperties(86, "Rn", "radon", 1.20, "#FFFF00"),

    # Period 7
    "Ac": ElementProperties(89, "Ac", "actinum", 1.95, "#649E72"),
    "Th": ElementProperties(90, "Th", "thorium", 1.80, "#25FD78"),
    "Pa": ElementProperties(91, "Pa", "protactinum", 1.80, "#29FA35"),
    "U": ElementProperties(92, "U", "uranium", 1.75, "#79A1AA"),
    "Np": ElementProperties(93, "Np", "neptunium", 1.75, "#4C4C4C"),
    "Pu": ElementProperties(94, "Pu", "plutonium", 1.75, "#4C4C4C"),
    "Am": ElementProperties(95, "Am", "americium", 1.75, "#4C4C4C"),
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

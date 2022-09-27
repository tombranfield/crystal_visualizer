# So what we want is to define
# Element("Mg") or Element(123) or Element("Magnesium")
# ie how to use multiple constructors in Python?
# Depending on supplied argument, uses the appropriate constructor
# Then constructs element object by referring to the table of constants
# containing the Element information
# So two issues
# How to write multiple constructors
# Where and how to write the table of chemical element information


from enum import Enum

class Element(Enum):
    """
    A class representing a chemical element.

    It consists of a symbol, a name, and an atomic number.
    """
    pass
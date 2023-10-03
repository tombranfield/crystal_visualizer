"""space_group.py"""


class SpaceGroup:
    """
    A space group representing symmetry of a repeating 3D pattern.

    In:
        The space group symbol in Hermann_Mauguin notation.

    """
    def __init__(self, symbol):
        """Initializes the space group using its symbol"""
        self._symbol = symbol

    @property
    def symbol(self):
        return self.symbol

    def __get_data(self):
        # Gets the data for the space group from the Internatinal
        # Tables of Crystallography
        pass

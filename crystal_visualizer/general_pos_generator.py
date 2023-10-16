"""general_positions"""


class GeneralPositions:
    """
    Generate a set of general positions given some starting atoms
    and a set of symmetry operations.
    """
    def __init(self, starting_atoms, symmetry_ops):
        self.starting_atoms = starting_atoms
        self.symmetry_ops = symmetry_ops

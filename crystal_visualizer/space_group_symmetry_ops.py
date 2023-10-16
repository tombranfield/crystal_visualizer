"""space_group_symmetry_ops"""


class SpaceGroupSymOps:
    """
    Represents the symmetry operations for generating general equivalent
    positions of a space group. 
    """
    def __init__(self, sym_ops=None):
        self._sym_ops = sym_ops

    @property
    def sym_ops(self):
        return self._sym_ops


if __name__ == "__main__":
    ops = [["x", "y", "z"], ["-x", "y", "z"]]
    my_sym_ops = SpaceGroupSymOps(ops)
    print(my_sym_ops.sym_ops)

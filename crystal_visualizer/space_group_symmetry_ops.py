"""space_group_symmetry_ops"""


from dataclasses import dataclass


@dataclass
class SpaceGroupSymOps:
    sym_ops: list[str]

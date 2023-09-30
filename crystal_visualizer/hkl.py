"""hkl.py"""

from dataclasses import dataclass


@dataclass
class HKL:
    """
    A dataclass representing the Miller Indices hkl
    """
    h: int
    k: int
    l: int

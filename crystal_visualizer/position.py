"""position.py"""


import numpy as np


class Position:
    """
    A class representing position.
    
    Args:
        x, y, z: floating point numbers representing the 
        fractional coordinates of the atom within the unit cell.
    """
    def __init__(self, x: float, y: float, z: float):
        """Initializes the Position class"""
        self.x = x
        self.y = y
        self.z = z

    def coods(self) -> np.array:
        """Returns the position vector of the array"""
        return np.array([self.x, self.y, self.z])
        
    def __eq__(self, other):
        if isinstance(other, Position):
            if (
                self.x == other.x 
                and self.y == other.y 
                and self.z == other.z
            ):
                return True
        return False

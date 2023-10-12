"""position.py"""


import numpy as np


class Position:
    """
    A class representing position.
    
    Args:
        fract_x, fract_y, fract_z: floating point numbers representing the 
        fractional coordinates of the atom within the unit cell.
    """
    def __init__(self, fract_x: float, fract_y: float, fract_z: float):
        """Initializes the Position class"""
        self.fract_x = fract_x
        self.fract_y = fract_y
        self.fract_z = fract_z

    @property
    def coods(self) -> np.array:
        """Returns the position vector of the array"""
        return np.array([self.fract_x, self.fract_y, self.fract_z])
        

"""crystal_plotter.py"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from crystal_visualizer.unit_cell import UnitCell




class CrystalPlotter:
    """
    Plots a crystal structure given its unit cell
    """
    def __init__(self, unit_cell: UnitCell):
        self.unit_cell = unit_cell




if __name__ == "__main__":
    print("hi")

"""crystal_plotter.py"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell
from crystal_visualizer.unit_cell import UnitCell




class CrystalPlotter:
    """
    Plots a crystal structure given its unit cell
    """
    def __init__(self, unit_cell: UnitCell):
        self.unit_cell = unit_cell
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})

    def plot(self):
        list_centre = []
        list_radius = []
        list_colour = []
        for atom in self.unit_cell.atoms:
            list_centre.append(atom.position_vector())
            list_radius.append(atom.element.atomic_radius)
            list_colour.append(atom.element.colour)

        print(list_centre)
        print(list_radius)
        print(list_colour)



if __name__ == "__main__":
    unit_cell = cif_to_unit_cell("Cu.cif")
    unit_cell.print_info()

    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()

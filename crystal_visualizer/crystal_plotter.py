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

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        for atom in self.unit_cell.atoms:
            radius = 0.5 * atom.element.atomic_radius
            a = self.unit_cell.lattice_param.length_a
            b = self.unit_cell.lattice_param.length_a
            c = self.unit_cell.lattice_param.length_a
            u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
            x = radius * np.cos(u) * np.sin(v)
            y = radius * np.sin(u) * np.sin(v)
            z = radius * np.cos(v)
            ax.plot_surface(x - a * atom.position.x,
                            y - b * atom.position.y,
                            z - c * atom.position.z,
                            color=atom.element.colour)
        plt.show()




if __name__ == "__main__":
    unit_cell = cif_to_unit_cell("YBa2Cu3O7-x.cif")
    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()

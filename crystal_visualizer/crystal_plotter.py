#TODO draw the unit cell edges
#TODO handle non-orthogonal coordinates
#TODO fix the positions - they're plotted as negative


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
        ax = fig.add_subplot(aspect="equal", projection="3d")

        # TODO refactor this, obviously
        # Plot the spheres
        for atom in self.unit_cell.atoms:
            radius = 0.5 * atom.element.atomic_radius
            a = self.unit_cell.lattice_param.length_a
            b = self.unit_cell.lattice_param.length_b
            c = self.unit_cell.lattice_param.length_c
            alpha = self.unit_cell.lattice_param.angle_alpha
            beta = self.unit_cell.lattice_param.angle_beta
            gamma = self.unit_cell.lattice_param.angle_gamma

            u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
            x = radius * np.cos(u) * np.sin(v)
            y = radius * np.sin(u) * np.sin(v)
            z = radius * np.cos(v)
            ax.plot_surface(a * atom.position.x - x,
                            b * atom.position.y - x,
                            c * atom.position.z - z,
                            color=atom.element.colour)
        
        # Plot cell edges (lines)
        # Start with a single line in orthogonal space
        x = np.array([0, a])
        y = np.array([0, 0])
        z = np.array([0, 0])
        ax.plot3D(x, y, z)

        # Plot appearance
        z_stretch_ratio = c / a
        ax.set_box_aspect((1, 1, z_stretch_ratio))
        ax.set_xlabel("a / r’$\AA$’")
        ax.set_ylabel("b / r’$\AA$’")
        ax.set_zlabel("c / r’$\AA$’")

        plt.show()




if __name__ == "__main__":
    unit_cell = cif_to_unit_cell("YBa2Cu3O7-x.cif")
    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()

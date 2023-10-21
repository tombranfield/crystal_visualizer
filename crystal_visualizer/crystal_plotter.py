#TODO handle non-orthogonal coordinates
#TODO refactor

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
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(aspect="equal", projection="3d")

        # Plot the spheres
        for atom in self.unit_cell.atoms:
            radius_scale = 0.35
            radius = radius_scale * atom.element.atomic_radius
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
                            b * atom.position.y - y,
                            c * atom.position.z - z,
                            color=atom.element.colour)
        
        # Plot the edges of the unit cell
        lines = [
            [(0, a), (0, 0), (0, 0)],  [(0, 0), (0, b), (0, 0)],
            [(a, a), (0, b), (0, 0)],  [(0, a), (b, b), (0, 0)],
            [(0, 0), (0, 0), (0, c)],  [(0, 0), (b, b), (0, c)],
            [(a, a), (0, 0), (0, c)],  [(a, a), (b, b), (0, c)],
            [(0, a), (0, 0), (c, c)],  [(0, 0), (0, b), (c, c)],
            [(a, a), (0, b), (c, c)],  [(0, a), (b, b), (c, c)],
        ]
        for line in lines:
            x, y, z = line[0], line[1], line[2]
            ax.plot3D(x, y, z, color="red")


        # Plot appearance
        z_stretch_ratio = c / a
        ax.set_box_aspect((1, 1, z_stretch_ratio))
        ax.set_xlabel("a / r’$\AA$’")
        ax.set_ylabel("b / r’$\AA$’")
        ax.set_zlabel("c / r’$\AA$’")
        fig.tight_layout()
        plt.show()




if __name__ == "__main__":
    unit_cell = cif_to_unit_cell("SrTiO3.cif")
    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()

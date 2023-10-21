"""crystal_plotter.py"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from crystal_visualizer.basis_vectors import BasisVectors
from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell
from crystal_visualizer.unit_cell import UnitCell


class CrystalPlotter:
    """
    Plots a crystal structure given its unit cell
    """
    def __init__(self, unit_cell: UnitCell):
        self.unit_cell = unit_cell
        self.basis_vectors = BasisVectors(unit_cell.lattice_param)

    def plot(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(aspect="equal", projection="3d")

        a = list(self.basis_vectors.a)
        b = list(self.basis_vectors.b)
        c = list(self.basis_vectors.c)

        lines = [
            [(0, 1), (0, 0), (0, 0)],  [(0, 0), (0, 1), (0, 0)],
            [(1, 1), (0, 1), (0, 0)],  [(0, 1), (1, 1), (0, 0)],
            [(0, 0), (0, 0), (0, 1)],  [(0, 0), (1, 1), (0, 1)],
            [(1, 1), (0, 0), (0, 1)],  [(1, 1), (1, 1), (0, 1)],
            [(0, 1), (0, 0), (1, 1)],  [(0, 0), (0, 1), (1, 1)],
            [(1, 1), (0, 1), (1, 1)],  [(0, 1), (1, 1), (1, 1)],
        ]

        # Plot the unit cell edges
        basis_vec = [a, b, c]
        for line in lines:
            r_before = np.dot(basis_vec, [line[0][0], line[1][0], line[2][0]])
            r_after = np.dot(basis_vec, [line[0][1], line[1][1], line[2][1]])
            x = (r_before[0], r_after[0])
            y = (r_before[1], r_after[1])
            z = (r_before[2], r_after[2])
            ax.plot3D(x, y, z, color="red")



        # Plot the spheres
        for atom in self.unit_cell.atoms:
            radius_scale = 0.4
            radius = radius_scale * atom.element.atomic_radius
            fract_pos = list(atom.position_vector())
            pos = np.dot([a, b, c], fract_pos)
            atom_x = pos[0]
            atom_y = pos[1]
            atom_z = pos[2]

            u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
            x = radius * np.cos(u) * np.sin(v)
            y = radius * np.sin(u) * np.sin(v)
            z = radius * np.cos(v)
            ax.plot_surface(pos[0] - x,
                            pos[1] - y,
                            pos[2] - z,
                            color=atom.element.colour)


        # Plot appearance
        z_stretch_ratio = np.linalg.norm(c) / np.linalg.norm(a)
        ax.set_box_aspect((1, 1, z_stretch_ratio))
        ax.set_xlabel("a / $\AA$")
        ax.set_ylabel("b / $\AA$")
        ax.set_zlabel("c / $\AA$")
        fig.tight_layout()
        plt.show()




if __name__ == "__main__":
    unit_cell = cif_to_unit_cell("SiO2.cif")
    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()

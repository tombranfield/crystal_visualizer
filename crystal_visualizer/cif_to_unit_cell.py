"""cif_to_unit_cell.py"""


from crystal_visualizer.atom import Atom
from crystal_visualizer.cif_reader import CifReader
from crystal_visualizer.general_pos_generator import GeneralPositionsGenerator
from crystal_visualizer.unit_cell import UnitCell


def cif_to_unit_cell(cif_filename) -> UnitCell:
    """
    Takes a cif and generates a unit cell
    """
    cif_reader = CifReader(cif_filename)
    cif_atoms = cif_reader.atoms
    symmetry_ops = cif_reader.symmetry_ops.sym_ops
    atoms = []
    for atom in cif_atoms:
        pos_gen = GeneralPositionsGenerator(atom, symmetry_ops)
        gen_positions = pos_gen.generate_positions()
        for gen_pos in gen_positions:
            atoms.append(Atom(atom.symbol, gen_pos.x, gen_pos.y, gen_pos.z))
    unit_cell = UnitCell(atoms, cif_reader.lattice_parameters)
    return unit_cell



if __name__ == "__main__":
    cif_file = "Cu.cif"
    unit_cell = cif_to_unit_cell(cif_file)
    unit_cell.print_info()




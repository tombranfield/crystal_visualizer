"""run.py"""

from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell




# Have a loop where the user chooses the structure

cif_file = "Cu.cif"
unit_cell = cif_to_unit_cell(cif_file)
unit_cell.print_info()

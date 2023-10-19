"""run.py"""

from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell


STRUCTURES = [
    "Cu",      "NaCl",     "CaF2",  "C",
    "SrTiO3",  "MgAl2O4",  "SiO2",  "YBa2Cu3O7-x",
]


def main():
    for structure in STRUCTURES:
        cif_file = structure + ".cif"
        unit_cell = cif_to_unit_cell(cif_file)
        unit_cell.print_info()
        print("\n\n\n")



if __name__ == "__main__":
    main()

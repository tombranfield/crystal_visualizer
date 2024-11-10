"""run.py"""


import sys

from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell
from crystal_visualizer.crystal_plotter import CrystalPlotter


STRUCTURES = [
    "Cu",      "NaCl",     "CaF2",  "C",
    "SrTiO3",  "MgAl2O4",  "SiO2",  "YBa2Cu3O7-x",
]


def print_choices(message):
    for count, structure in enumerate(STRUCTURES, 1):
        print(f"  ({count}): {structure}")
    print("Choose a structure or display or enter 'q' to quit.")
    if message: print(message)


def get_user_response():
    prompt = "> "
    return input(prompt)


def check_for_quit(user_response):
    if user_response.lower() in ["q", "quit", "exit"]:
        sys.exit()


def plot_crystal(structure_str: str):
    print("Generating crystal. This may take a few seconds...")
    cif_filename = structure_str + ".cif"
    unit_cell = cif_to_unit_cell(cif_filename)
    crystal_plotter = CrystalPlotter(unit_cell)
    crystal_plotter.plot()


def main():
    message = ""
    while True:
        print_choices(message)
        user_response = get_user_response()
        check_for_quit(user_response)
        try:
            user_response = int(user_response)
        except ValueError:
            message = "Enter an integer between 1 and " + str(len(STRUCTURES))
        else:
            if 1 <= user_response <= len(STRUCTURES):
                message = ""
                structure_str = STRUCTURES[user_response - 1]
                plot_crystal(structure_str)
            else:
                message = "Enter an integer between 1 and " + str(len(STRUCTURES))


if __name__ == "__main__":
    main()

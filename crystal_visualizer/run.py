"""run.py"""

from crystal_visualizer.cif_to_unit_cell import cif_to_unit_cell
from crystal_visualizer.crystal_plotter import CrystalPlotter


STRUCTURES = [
    "Cu",      "NaCl",     "CaF2",  "C",
    "SrTiO3",  "MgAl2O4",  "SiO2",  "YBa2Cu3O7-x",
]


def print_choices():
    for count, structure in enumerate(STRUCTURES, 1):
        print(f"  ({count}): {structure}")
    print("Choose a structure or display or enter 'q' to quit.")


def get_user_response():
    message = "> "
    return input(message)



def main():
    while True:
        print_choices()
        user_response = get_user_response()
        if user_response.lower() in ["q", "quit", "exit"]:
            break
        try:
            user_response = int(user_response)
        except ValueError:
            print(f"Enter an integer between 1 and {len(STRUCTURES)}")
        else:
            if 1 <= user_response <= len(STRUCTURES):
                print("Generating crystal. This may take a few seconds...")
                cif_filename = STRUCTURES[user_response - 1] + ".cif"
                unit_cell = cif_to_unit_cell(cif_filename)
                crystal_plotter = CrystalPlotter(unit_cell)
                crystal_plotter.plot()
            else:
                print(f"Enter an integer between 1 and {len(STRUCTURES)}")


if __name__ == "__main__":
    main()

"""test_cif_reader.py"""


from pathlib import Path
import pytest


CIF_PATH = str( Path(__file__).parents[1] / "data" / "cif_files")



if __name__ == "__main__":
    print(CIF_PATH)

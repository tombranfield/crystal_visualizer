from collections import namedtuple
from typing import Union

# Put element properties into a named tuple
Element = namedtuple("Element", ["atomic_number", "symbol", "name"])

# Period 1
H = Element(1, "H", "hydrogen")
He = Element(2, "He", "helium")

# Period 2
Li = Element(3, "Li", "lithium")
Be = Element(4, "Be", "beryllium")
B = Element(5, "B", "boron")
C = Element(6, "C", "carbon")
N = Element(7, "N", "nitrogen")
O = Element(8, "O", "oxygen")
F = Element(9, "F", "fluorine")
Ne = Element(10, "Ne", "neon")

# Period 3
Na = Element(11, "Na", "sodium")
Mg = Element(12, "Mg", "magnesium")
Al = Element(13, "Al", "aluminium")
Si = Element(14, "Si", "silicon")
P = Element(15, "P", "phosphorus")
S = Element(16, "S", "sulphur")
Cl = Element(17, "Cl", "chlorine")
Ar = Element(18, "Ar", "argon")

# Period 4
K = Element(19, "K", "potassium")
Ca = Element(20, "Ca", "calcium")
Sc = Element(21, "Sc", "scandium")
Ti = Element(22, "Ti", "titanium")
V = Element(23, "V", "vanadium")
Cr = Element(24, "Cr", "chromium")
Mn = Element(25, "Mn", "manganese")
Fe = Element(26, "Fe", "iron")
Co = Element(27, "Co", "cobalt")
Ni = Element(28, "Ni", "nickel")
Cu = Element(29, "Cu", "copper")
Zn = Element(30, "Zn", "zinc")
Ga = Element(31, "Ga", "gallium")
Ge = Element(32, "Ge", "germanium")
As = Element(33, "As", "arsenic")
Se = Element(34, "Se", "selenium")
Br = Element(35, "Br", "bromine")
Kr = Element(36, "Kr", "krypton")


# A tuple containing the element symbols in ascending atomic number
# The tuple index corresponds to the atomic number
ELEMENTS = (
    None,
    H, He,
    Li, Be, B, C, N, O, F, Ne,
    Na, Mg, Al, Si, P, S, Cl, Ar,
    K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr,
    Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe,
    Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn,
    Fr, Ra, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og
)

class Element:
    """A class representing a chemical element."""
    def __init__(self, in_param: Union[str, int]):
        """Initialize the element using its symbol, name, or atomic number"""
        if isinstance(in_param, str):
            if len(str) == 1 or len(str) == 2:
                # Create an element with the symbol
            else:
                # Create an element with its name
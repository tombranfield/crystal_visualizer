"""
This module contains the Element class that represents a chemical element
for each atom within a crystal structure.

The user can assign a chemical element using either its symbol or its atomic
number, for example by assigning self.element = Element("Ba") or
self.element = Element(56).

Properties of the element such as the atomic number or element name can be
retrieved using self.element.atomic_number or self.element.name, for example.
"""

from collections import namedtuple
from typing import Union

# Put element properties into a named tuple for readability and immutability
# Using namedtuple also allows extra properties (eg molar mass or electronic
# configuration) to be added in the future, if necessary.
# For now, only the symbol, name, and atomic number is necessary.
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

# Period 5
Rb = Element(37, "Rb", "rubidium")
Sr = Element(38, "Sr", "strontium")
Y = Element(39, "Y", "yttrium")
Zr = Element(40, "Zr", "zirconium")
Nb = Element(41, "Nb", "niobium")
Mo = Element(42, "Mo", "molybdenum")
Tc = Element(43, "Tc", "technetium")
Ru = Element(44, "Ru", "ruthenium")
Rh = Element(45, "Rh", "rhodium")
Pd = Element(46, "Pd", "palladium")
Ag = Element(47, "Ag", "silver")
Cd = Element(48, "Cd", "cadmium")
In = Element(49, "In", "indium")
Sn = Element(50, "Sn", "tin")
Sb = Element(51, "Sb", "antimony")
Te = Element(52, "Te", "tellurium")
I = Element(53, "I", "iodine")
Xe = Element(54, "Xe", "xenon")

# Period 6
Cs = Element(55, "Cs", "caesium")
Ba = Element(56, "Ba", "barium")
La = Element(57, "La", "lanthanum")
Ce = Element(58, "Ce", "cerium")
Pr = Element(59, "Pr", "praesodymium")
Nd = Element(60, "Nd", "neodymium")
Pm = Element(61, "Pm", "promethium")
Sm = Element(62, "Sm", "samarium")
Eu = Element(63, "Eu", "europium")
Gd = Element(64, "Gd", "gadolinium")
Tb = Element(65, "Tb", "terbium")
Dy = Element(66, "Dy", "dysprosium")
Ho = Element(67, "Ho", "holmium")
Er = Element(68, "Er", "erbium")
Tm = Element(69, "Tm", "thulium")
Yb = Element(70, "Yb", "ytterbium")
Lu = Element(71, "Lu", "lutetium")
Hf = Element(72, "Hf", "hafnium")
Ta = Element(73, "Ta", "tantalum")
W = Element(74, "W", "tungsten")
Re = Element(75, "Re", "rhenium")
Os = Element(76, "Os", "osmium")
Ir = Element(77, "Ir", "iridium")
Pt = Element(78, "Pt", "platinum")
Au = Element(79, "Au", "gold")
Hg = Element(80, "Hg", "mercury")
Tl = Element(81, "Tl", "thallium")
Pb = Element(82, "Pb", "lead")
Bi = Element(83, "Bi", "bismuth")
Po = Element(84, "Po", "polonium")
At = Element(85, "At", "astatine")
Rn = Element(86, "Rn", "radon")




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
    def __init__(self, chemical_symbol: str):
        """Initialize the element using its chemical symbol """
        self.symbol = chemical_symbol

    # This is a read-only property
    @property
    def chemical_symbol(self):
        """Returns the chemical symbol of the element"""
        return self._chemical_symbol
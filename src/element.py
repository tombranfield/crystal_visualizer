from collections import namedtuple
from typing import Union

ELEMENTS = (
    H, He,
    Li, Be, B, C, N, O, F, Ne,
    Na, Mg, Al, Si, P, S, Cl, Ar,
    K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr,
    Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe,
    Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn,
    Fr, Ra, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og
)



# Put element properties into a named tuple
Element = namedtuple("Element", ["atomic_number", "symbol", "name"])

H = Element(1, "H", "hydrogen")
He = Element(2, "He", "helium")

Li = Element(3, "Li", "lithium")



class Element:
    """A class representing a chemical element."""
    def __init__(self, in_param: Union[str, int]):
        """Initialize the element using its symbol, name, or atomic number"""
        if isinstance(in_param, str):
            if len(str) == 1 or len(str) == 2:
                # Create an element with the symbol
            else:
                # Create an element with its name
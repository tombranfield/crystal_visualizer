# crystal_visualizer

A program for generating and examining crystal structures

The program loads a .cif file, parses it, then uses space group 
information to generate the crystal structure using symmetry. Bond
lengths and angle are calculated using metric tensor methods with 
NumPy and the final structure is displayed using Matplotlib. And 
everything is tested using Pytest :)

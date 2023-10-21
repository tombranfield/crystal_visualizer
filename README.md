# Crystal Visualizer

A program for generating and examining crystal structures

The program loads a crystallography .cif file, parses it, then uses space group 
information to generate the crystal structure using symmetry

Bond lengths and angles are calculated using metric tensor methods with 
NumPy, and the final structure is displayed using Matplotlib with mplot3d

Tests are performed using Pytest with a code coverage of 90+%

![preview](https://github.com/tombranfield/crystal_visualizer/blob/main/crystal_visualizer_preview.jpg)



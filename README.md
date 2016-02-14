# ASPycross
Picross solver using Answer Set Programming and Python

# What? Why?
My passion for puzzles and, in particular, Picross (aka Nonograms) derived in the challenge of implementing a simple picross solver using Answer Set Programming due to it's flexibility and succesfulness with many other puzzles. Particularly for this project we'll be using the grounder gringo and the clasp solver grouped in the tool clingo. 

The challenge consists of many parts:
 - Creating the solver in ASP to solve any correct Picross out there
 - Make it usable and nice through python
 - Implement a web interface to input the puzzles in a user-friendly way
 - See if we can implement some Artificial Vision to the system and enable input through a picture of a Picross puzzle.

# Installation
Download clingo 3.0.5 from the Potassco group's sourceforge and add it to the path, make sure that you have python 2.7 up and running in your system and then call `python aspycross /path/to/your/puzzle.lp`

# ASPycross
Picross solver using Answer Set Programming and Python

# What? Why?
My passion for puzzles and, in particular, Picross (aka Nonograms) derived in the challenge of implementing a simple picross solver using Answer Set Programming due to it's flexibility and succesfulness with many other puzzles. Particularly for this project we'll be using the grounder gringo and the clasp solver grouped in the tool clingo.

# What's working
Right now, ASPycross is a command line tool that takes any Picross puzzle in the form os ASP facts (see examples in input folder) and pretty-prints the solution.
The current work is focused on making it Python3 compatible and developing a web GUI with Electron or some other serverless light web framework.

# Requirements
For the early Command Line versions you just need:
 - The latest version of clingo
 - Python 2.7

# Installation
Download the latest clingo from http://github.com/potassco/clingo and add it to the path or copy it to the ASPycross folder, make sure that you have python installed in your system and then call `python aspycross /path/to/your/puzzle.lp`

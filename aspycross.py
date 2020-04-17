# -*- coding: utf-8 -*-
"""Main script to start the resolution."""

import os
import argparse
import numpy as np

from clyngor import ASP, solve


def matrixstr(matrix, pos_symbol='o', neg_symbol='-'):
    """Print the matrix representation."""
    mstr = []
    for row in matrix:
        rstr = ""
        for col in row:
            rstr += pos_symbol if col else neg_symbol
        mstr.append(rstr)
    return '\n'.join(mstr)


def main():
    # Initialize the script parser
    txt = "Resolve a Picross problem and print the result."
    parser = argparse.ArgumentParser(description=txt)
    parser.add_argument("picross", help="route of the picross hints")

    # Get the parameters
    args = parser.parse_args()
    data = args.picross

    # Set the program path
    dirpath = os.path.dirname(os.path.abspath(__file__))
    program = os.path.join(dirpath, "picross_solve_block.lp")

    # Resolve the problem instance
    answers = solve(program, data, nb_model=1)
    answer = next(answers.by_predicate)

    # Get height and width
    height = next(iter(answer["maxheight"]))[0]
    width = next(iter(answer["maxwidth"]))[0]

    # Get colorated cells
    cells = answer["hcell"]

    # Construct the associated (complete) matrix
    matrix = np.zeros((height, width))
    for c in cells:
        matrix[c[1] - 1, c[0] - 1] = 1

    # Print the solution
    print("Solution :")
    print(matrixstr(matrix))



if __name__ == "__main__":
        main()

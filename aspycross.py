# -*- coding: utf-8 -*-
"""Main script to start the resolution."""

import os
import argparse
import numpy as np
from PIL import Image
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


def matrix_as_img(matrix, outputfile='img_picross.png', pixel_size=6):
    """Save the matrix as a black and white image."""
    colors = {
        'white': [255, 255, 255],
        'black': [0, 0, 0],
    }

    (height, width) = matrix.shape
    img_mat = np.zeros((height * pixel_size, width * pixel_size, 3))
    for row in range(height):
        rrow = (row * pixel_size, row * pixel_size + pixel_size)
        for col in range(width):
            rcol = (col * pixel_size, col * pixel_size + pixel_size)
            value = colors['black'] if matrix[row, col] else colors['white']
            img_mat[rrow[0]:rrow[1], rcol[0]: rcol[1], :] = value

    # Create and save the image
    img = Image.fromarray(img_mat.astype(np.uint8))
    img.save(outputfile)
    img.show()


def main():
    # Initialize the script parser
    txt = "Resolve a Picross problem and print the result."
    parser = argparse.ArgumentParser(description=txt)
    parser.add_argument("picross", help="route of the picross hints")
    parser.add_argument(
        "-img", "--image_output", default="",
        help="Path in which save the solution image (default: don't save it)"
    )
    parser.add_argument(
        "-px", "--pixel_size", type=int, default=6,
        help="Pixel size to use for the image (default: 6), only if -img is set"
    )

    # Get the parameters
    args = parser.parse_args()
    data = args.picross
    outputfile = args.image_output
    pixel_size = args.pixel_size

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

    # Save it as an image
    if outputfile:
        matrix_as_img(matrix, outputfile=outputfile, pixel_size=pixel_size)


if __name__ == "__main__":
        main()

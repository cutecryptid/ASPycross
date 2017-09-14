import argparse
from subprocess import Popen, PIPE
import re
import numpy as np

def matrixstr(m):
    mstr = ""
    for row in m:
        rstr = ""
        for c in row:
            if c == 1:
                rstr += "o"
            else:
                rstr += "x"
        rstr += "\n"
        mstr += rstr
    return mstr


parser = argparse.ArgumentParser()
parser.add_argument("picross", help="route of the picross hints")
parser.add_argument("-n", "--nsols", help="number of solutions, all displayed by default",
                    default=0)
args = parser.parse_args()

picross = args.picross

p = Popen(["clingo5", "picross_solve_block.lp", picross, "-n", str(args.nsols)],
            stdout=PIPE)
out, err = p.communicate()

solutions = re.split(r'Answer:\s[0-9]+\n', out)

info = solutions[0]
solutions = solutions[1:]

for idx,sol in enumerate(solutions):
    height = int(re.findall(r'maxheight\(([0-9]+)\)', sol)[0])
    width = int(re.findall(r'maxwidth\(([0-9]+)\)', sol)[0])
    matrix = np.zeros((height, width))
    cells = re.findall(r'hcell\(([0-9]+),([0-9]+)\)', sol)
    for c in cells:
        matrix[int(c[1])-1, int(c[0])-1] = 1
    print ("Solution #" + str(idx+1))
    print (matrixstr(matrix))
    print ("")

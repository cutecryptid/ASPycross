import argparse
import subprocess
import re

class Cell(object):
	"""Storage class for cells, just a symbol and a 2D position"""
	def __init__(self, symbol, row, col):
		self.symbol = symbol
		self.row = row
		self.col = col

	def __str__(self):
		return self.symbol

class PicrossSolution(object):
	"""Storage class for the picross solution"""
	def __init__(self, raw_sol):
		self.raw_sol = raw_sol
		self.cells = self.parse_solution()

	def parse_solution(self):
		out = self.raw_sol
		size_x = re.search('size_x\(([0-9]+)\)', out)
		size_y = re.search('size_y\(([0-9]+)\)', out)
		size_x = int(size_x.group(1))
		size_y = int(size_y.group(1))
		cells = re.findall('out_cell\(([xo]),([0-9]+),([0-9]+)\)', out)
		sol_cells = []
		for x in range(size_x):
			sol_cells += [[]]
			for y in range(size_y):
				sol_cells[x] += [0]
		for cell in cells:
			sol_cells[int(cell[1])-1][int(cell[2])-1] = Cell(cell[0], int(cell[1])-1, int(cell[2])-1)
		return sol_cells

	def __str__(self):
		ret_str = ""
		for row in self.cells:
			ret_str += "|"
			for cell in row:
				ret_str += str(cell)
			ret_str += "|\n"
		return ret_str
		
def main():
	parser = argparse.ArgumentParser(description='ASPycross - Picross solving with ASP and python')
	parser.add_argument('puzzle', metavar='XML_SCORE',
	                   help='input puzzle in ASP format for solving')
	parser.add_argument('-n', '--num_sols', metavar='N', nargs=1, default=1, type=int,
	                   help='max number of ASP solutions, by default all of them')

	args = parser.parse_args()

	infile = args.puzzle

	n = args.num_sols
	if args.num_sols != 1:
		n = args.num_sols[0]

	picross_args = ("clingo", infile,"picross.lp","-n", str(n))
	picross_proc = subprocess.Popen(picross_args, stdout=subprocess.PIPE)
	picross_out = picross_proc.stdout.read()

	print picross_out
	print "-------------------------"
	print PicrossSolution(picross_out)

	if (re.search("UNSATISFIABLE",picross_out) != None):
		sys.exit("UNSATISFIABLE, stopping execution.")

if __name__ == "__main__":
    main()
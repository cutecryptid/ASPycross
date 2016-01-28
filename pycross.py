import argparse
import subprocess
import re

		
def main():
	parser = argparse.ArgumentParser(description='ASPycross - Picross solving with ASP and python')
	parser.add_argument('puzzle', metavar='XML_SCORE',
	                   help='input puzzle in ASP format for solving')
	parser.add_argument('-n', '--num_sols', metavar='N', nargs=1, default=0, type=int,
	                   help='max number of ASP solutions, by default all of them')

	args = parser.parse_args()

	infile = args.puzzle

	n = args.num_sols
	if args.num_sols != 0:
		n = args.num_sols[0]

	picross_args = ("clingo", infile,"picross.lp","-n", str(n))

	picross_proc = subprocess.Popen(picross_args, stdout=subprocess.PIPE)
    
	picross_out = picross_proc.stdout.read()

	print picross_out

	if (re.search("UNSATISFIABLE",picross_out) != None):
		sys.exit("UNSATISFIABLE, stopping execution.")

if __name__ == "__main__":
    main()
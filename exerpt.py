import argparse
import os
from pydat import *

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str, help = "The file to extract lines from.")
parser.add_argument("-l", "--lines", type = int, default = 100, help = "The number of lines to take from the file.")
args = parser.parse_args()

if not os.path.exists(args.file):
	print("The specified file does not exist.")
	quit()

if os.path.isdir(args.file):
	print("The specified path points to a folder.")
	quit()

outFile = addExtStart(args.file, "exerpt-" + str(args.lines))

with open(args.file, "r") as input:
	with open(outFile, "w") as output:
		count = 0
		for line in input:
			output.write(line)

			count = count + 1
			if count >= args.lines:
				break

print("Created file: " + outFile)
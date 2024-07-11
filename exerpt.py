import argparse
import os
from pydat import *

def writeLines(input, output, count):
	for line in input:
		output.write(line)

		count = count - 1
		if count == 0:
			break

def writeLinesEnd(input, output, count):
	buffer = Buffer(count)

	for line in input:
		buffer.write(line)

	for line in buffer.get():
		output.write(line)

def skipLines(input, count):
	for line in input:
		count = count - 1
		if count == 0:
			break

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str, help = "The file to extract lines from.")
parser.add_argument("-l", "--lines", type = int, default = 100, help = "The number of lines to take from the file.")
parser.add_argument("-o", "--offset", type = int, default = 0, help = "The number of lines to skip at the start of the file. (incompatible with --reverse)")
parser.add_argument("-hr", "--header", type = int, default = 0, help = "The number of header rows to keep.")
parser.add_argument("-r", "--reverse", action = "store_true", help = "Read lines from the end of the file. (incompatible with --offset)")
args = parser.parse_args()

if not os.path.exists(args.file):
	print("The specified file does not exist.")
	quit()

if os.path.isdir(args.file):
	print("The specified path points to a folder.")
	quit()

if args.lines < 0:
	print("The number of lines can't be negative.")
	quit()

if args.offset < 0:
	print("The line offset can't be negative.")
	quit()

if args.reverse and args.offset > 0:
	print("-r/--reverse and -o/--offset are mutually exclusive options.")
	quit()

outFile = None
if args.offset == 0:
	outFile = addExtStart(args.file, "exerpt-" + str(args.lines))
else:
	outFile = addExtStart(args.file, "exerpt-" + str(args.offset) + "-" + str(args.lines))

with open(args.file, "r") as input:
	with open(outFile, "w") as output:
		if args.header > 0:
			writeLines(input, output, args.header)

		if args.offset > 0:
			skipLines(input, args.offset)

		if args.reverse:
			writeLinesEnd(input, output, args.lines)
		else:
			writeLines(input, output, args.lines)

print("Created file: " + outFile)
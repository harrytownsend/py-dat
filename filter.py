import argparse
import os
import re
from pydat import *

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str, help = "The file to filter.")
parser.add_argument("-a", "--append", action = "store_true", help = "Append lines to the output file.")
parser.add_argument("-d", "--delimiter", type = str, help = "The character sequence delimiting fields.")
parser.add_argument("-f", "--field", type = str, help = "The field to search in. (@ prefix for field names)")
parser.add_argument("-hr", "--header", action = "store_true", help = "Header row present in file.")
parser.add_argument("-q", "--quote", type = str, help = "The quote character")
parser.add_argument("-re", "--regex", type = str, help = "The regular expression to seach for on each line.")
parser.add_argument("-s", "--search", type = str, help = "The literal string to search for on each line.")
args = parser.parse_args()

if not os.path.exists(args.file):
	print("The specified file does not exist.")
	quit()

if os.path.isdir(args.file):
	print("The speficied path is a directory.")
	quit()

if args.search is None and args.regex is None:
	print("A search criteria was not specified.")
	quit()

if args.search is not None and args.regex is not None:
	print("Both a literal search string and a regular expression search string were provided.")
	quit()

isCSV = args.delimiter is not None

outputFilename = addExtStart(args.file, "filter")

with open(args.file, "r") as input:
	with open(outputFilename, "w") as output:
		for line in input:
			isMatch = False

			if isCSV:
				fields = CSVLine(line, args.delimiter, args.quote)

				min = 0
				max = fields.length()
				if args.field:
					if args.field.isnumeric():
						min = int(args.field) - 1
						max = min + 1

				for i in range(min, max):
					field = fields.get(i)

					if args.search is not None:
						if field.find(args.search) >= 0:
							isMatch = True
							break
					else:
						if re.search(args.regex, field):
							isMatch = True
							break

			else:
				if args.search is not None:
					if line.find(args.search) >= 0:
						isMatch = True
				else:
					if re.search(args.regex, line):
						isMatch = True

			if isMatch:
				output.write(line)
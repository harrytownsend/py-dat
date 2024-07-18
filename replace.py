import argparse
import os
import re
from pydat import *

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str, help = "The file to replace data in.")
parser.add_argument("find", type = str, help = "The sequence to find.")
parser.add_argument("replace", type = str, help = "The sequence to replace with.")
parser.add_argument("-o", "--output", type = str, help = "The file to output the results to.")
parser.add_argument("-re", "--regex", action = "store_true", help = "Treat the sequence to find as a regular expression.")
parser.add_argument("-l1", "--line-first", action = "store_true", help = "Only replace the first instance in the line.")
args = parser.parse_args()

if not os.path.exists(args.file):
	print("The specified file does not exist.")
	quit()

if os.path.isdir(args.file):
	print("The specified path points to a folder.")
	quit()

outputFilename = args.output
if outputFilename is None:
	outputFilename = addExtStart(args.file, "replace")

outputDir = os.path.dirname(outputFilename)
if outputDir != "" and not os.path.exists(outputDir):
	print("The directory for the output folder does not exist.")
	quit()

if os.path.isdir(outputFilename):
	print("The output file already exists as a directory: " + outputFilename)
	quit()

replace = args.replace
replace = bytes(replace, "utf-8").decode("unicode_escape")
replace = bytes(replace, "utf-8").decode("unicode_escape")

with open(args.file, "r") as input:
	with open(outputFilename, "w") as output:
		for line in input:
			if args.regex:
				if args.line_first:
					line = re.sub(args.find, replace, line, 1)
				else:
					line = re.sub(args.find, replace, line)
			else:
				if args.line_first:
					line = line.replace(args.find, replace, 1)
				else:
					line = line.replace(args.find, replace)

			output.write(line)
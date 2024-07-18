import argparse
import os
import pydat

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str, help = "The file to describe.")
args = parser.parse_args()

if not os.path.exists(args.file):
	print("The specified file does not exist.")
	quit()

if os.path.isdir(args.file):
	print("The speficied path is a directory.")
	quit()

lines = 0
characters = 0

with open(args.file, "r") as input:
	for line in input:
		lines += 1
		characters += len(line)

print("Lines: " + str(lines))
print("Characters: " + str(characters))
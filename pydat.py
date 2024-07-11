import os

def addExtStart(path, extension):
	file = os.path.basename(path)
	dir = os.path.dirname(path)

	index = file.find(".")
	if index >= 0:
		file = file[0:index] + "." + extension + file[index:]
	else:
		file = file + "." + extension

	return os.path.join(dir, file)
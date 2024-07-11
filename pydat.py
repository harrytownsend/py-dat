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

class Buffer:

	def __init__(self, size):
		self._size = size
		self._length = 0
		self._head = 0

		self._list = []

	def get(self):
		if(self._length < self._size):
			return list(self._list)
		else:
			return self._list[self._head:self._size] + self._list[0:self._head]

	def length(self):
		return self._length

	def size(self):
		return self._size
	
	def write(self, item):
		if(self._length < self._size):
			self._list.append(item)
			self._length = self._length + 1
		else:
			self._list[self._head] = item

		self._head = (self._head + 1) % self._size
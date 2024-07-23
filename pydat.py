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

class CSVLine:

	def __init__(self, line, delimiter = ",", quote = None):
		self._line = line
		self._delimiter = delimiter
		self._quote = quote
		self._fields = []

		if self._line.endswith("\r\n"):
			self._line = self._line[0 : len(self._line) - 2]
		elif self._line.endswith("\n"):
			self._line = self._line[0 : len(self._line) - 1]

		self._readLine()

	def get(self, position):
		return self._fields[position]
	
	def length(self):
		return len(self._fields)

	def _readLine(self):
		position = 0
		length = len(self._line)

		read = True
		while read:
			position = self._skipWhitespace(position)

			if position < length:
				end = self._readField(position)
				field = self._line[position:end]

				if self._quote is not None and field.startswith(self._quote) and field.endswith(self._quote):
					field = field[1 : len(field) - 1]

				self._fields.append(field)

				position = end + 1
			else:
				read = False

	def _readField(self, offset):
		length = len(self._line)

		isQuoted = False
		if self._quote is not None and self._quote == self._line[offset]:
			isQuoted = True
			offset += 1

		while offset < length:
			char = self._line[offset]

			if char == "\\":
				offset += 1
			elif (isQuoted and char == self._quote) or (not isQuoted and char == ","):
				return offset

			offset += 1

		return offset
		
	def _skipWhitespace(self, offset):
		length = len(self._line)

		while offset < length and self._line[offset].isspace():
			offset += 1

		return offset


class ArrayQueue:
	def __init__(self, capacity = 20):
		self._data = []
		self._size = 0
		self._capacity = capacity

	def enqueue(self, person):
		self._size += 1
		self._data.insert(0, person)

	#return self.sz < max queue size
	def availableSpace(self):
		return self._size < self.capacity()

	def dequeue(self):
		self._size -= 1
		return self._data.pop()

	def capacity(self):
		return self._capacity

	def size(self):
		return self._size

	def isEmpty(self):
		return self._size == 0

	def getQueue(self):
		return self._data

	def contains(self, person):
		return self.indexOf(person) >= 0

	def indexOf(self, person):
		s = self.size()
		i = 0
		while i < s:
			if self._data[i].id == person.id:
				return i
			i += 1
		return -1
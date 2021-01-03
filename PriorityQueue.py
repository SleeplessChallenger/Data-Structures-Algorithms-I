
#will imlpement MinBinaryHeap
#the lower the .priority the bigger importance

from math import floor
class Node:

	def __init__(self,val,priority):
		self.val = val
		self.priority = priority


class PriorityQueue:

	def __init__(self):
		self.values = []

	def enqueue(self,value,priority):
		node = Node(value,priority)
		self.values.append(node)
		self.bubbleUp()

	def bubbleUp(self):
		idx = len(self.values) - 1
		element = self.values[idx]
		while idx > 0:
			parentIdx = floor((idx - 1)/2)
			parent = self.values[parentIdx]
			if element.priority <= parent.priority: 
				break
			self.values[idx] = parent
			self.values[parentIdx] = element
			idx = parentIdx

	def dequeue(self):
		node = self.values[0]
		end = self.values.pop()
		if len(self.values) > 1:
			self.values[0] = end
			self.percolate()
		return node

	def percolate(self):
		idx = 0
		element = self.values[0]
		length = len(self.values)
		while True:
			leftIdx = 2 * idx + 1
			rightIdx = 2 * idx + 2
			swap = None
			if leftIdx < length:
				leftChild = self.values[leftIdx]
				if leftChild.priority < element.priority:
					swap = leftIdx

			if rightIdx < length:
				rightChild = self.values[rightIdx]
				if (swap == None and rightChild.priority < element.priority) or (swap != None and rightChild.priority < leftChild.priority):
					swap = rightIdx

			if swap == None:
				break

			self.values[idx] = self.values[swap]
			self.values[swap] = element

			idx = swap
			



queue = PriorityQueue()

queue.enqueue(5,2)




































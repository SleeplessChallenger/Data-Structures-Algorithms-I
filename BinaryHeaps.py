#In a MaxBinaryHeap, parent nodes are always larger than child nodes. 
#In a MinBinaryHeap, parent nodes are always smaller than child nodes
#But there are no guarantees between sibling nodes

#Binary heaps are used to implement Priority Queues, which
#are very commonly used data structures

#To find child from parent: Left Child is (2n + 1) and Right Child is (2n + 2)
#And to find parent: (n - 1)/2 floored - to find Parent from Child
#Aforementioned stuff is done to indices of nodes not the values of nodes

#BinaryHeaps
#Insertion O(log n)  Even with worst case it will be O(log n) while Binary Tree can be O(n)
#Removal O(log n)
#Search O(n)   For searching BinaryTree is much better
#for 16 elements 4 comparisions


from math import floor
class MaxBinaryHeap:

	def __init__(self):
		self.values = []

	#mine
	def insert(self,val):
		self.values.append(val)
		index = len(self.values) - 1
		parentindex = floor((index - 1)/2)
		while index > 0:
			if self.values[index] > self.values[parentindex]:
				self.values[index], self.values[parentindex] = self.values[parentindex], self.values[index]
				index = parentindex
				parentindex = floor((index - 1)/2)
			else:
				break
	#with varibale
		self.heap.append(val)
		ind = len(self.heap) - 1
		element = self.heap[ind]
		while ind > 0:
			parentInd = floor((ind - 1)/2)
			if element > self.heap[parentInd]:
				self.heap[ind] = self.heap[parentInd]
				self.heap[parentInd] = element
				ind = parentInd
				element = self.heap[ind]
			else:
				break
		print(self.heap)



	def remove(self):
		max_ = self.values[0]
		end = self.values.pop()
		if len(self.values) > 0:
			self.values[0] = end
			self.sinkDown()
		print(self.values)
		return max_

	def sinkDown(self):
		idx = 0
		length = len(self.values)
		element = self.values[0]
		#we swapped the child and element,
		#but the variable 'first' [element] will keep the value for further possible swaps\
		#And it's index position is kept in idx
		while True:
			leftIdx = 2 * idx + 1
			rightIdx = 2 * idx + 2
			swap = None
			if leftIdx < length:
				leftChild = self.values[leftIdx]
				if leftChild > element:
					swap = leftIdx
			if rightIdx < length:
				rightChild = self.values[rightIdx]
				if (swap == None and rightChild > element) or (swap != None and rightChild > leftChild):
						swap = rightIdx

			if swap == None:
				break
			self.values[idx] = self.values[swap]
			self.values[swap] = element
			idx = swap

	#Colt's solution
	# def insert(self,var):
	# 	self.values.append(var)
	# 	self.bubbleUp()

	# def bubbleUp(self):
	# 	index = (len(self.values) - 1)
	# 	while index > 0:
	# 		parentInd = floor((index - 1)/2)
	# 		if self.values[parentInd] >= self.values[index]:
	# 			break
	# 		self.values[parentInd], self.values[index] = self.values[index], self.values[parentInd]
	# 		index = parentInd

	def remove(self):
		node = self.values.pop()
		end = self.values[0]
		if len(self.values) > 0:
			self.values[0] = node
			self.bubbleValue()
		return end

	def bubbleValue(self):
		idx = 0
		element = self.values[0]
		length = len(self.values)
		while True:
			leftIdx = 2 * idx + 1
			rightIdx = 2 * idx + 2
			swap = None
			if leftIdx < length:
				leftChild = self.values[leftIdx]
				if leftChild > element:
					swap = leftIdx

			if rightIdx < length:
				rightChild = self.values[rightIdx]
				if (rightChild > element and swap == None) or (rightChild > leftChild and swap != None):
					swap = rightIdx

			if swap == None:
				break

			self.values[idx] = self.values[swap]
			self.values[swap] = element
			idx = swap



heap = MaxBinaryHeap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.insert(55)
heap.remove()





























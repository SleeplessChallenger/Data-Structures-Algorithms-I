q = []

q.append('First')
q.append('Second')
q.append('Third')

q.pop(0)
q.pop(0)
q.pop(0)

#Queue is also a way of just imlementing particular structure.
#Here FIFO is used: First in first out
#So as not to reindex the whole array it's much better to insert in the
#beginning and remove from the end using 
#python(insert with index 0 and pop) & JS(unshift and pop) in
#!!!!!array
#But in Singly Linked List we've opted for adding to the end and removing 
#from start

q.insert(0,'First')
q.insert(0,'Second')
q.insert(0,'Third')



class Node:

	def __init__(self,val):
		self.val = val
		self.next = None


class Queue:

	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def enqueue(self,var):
		var = Node(var)
		if not self.first:
			self.first = var
			self.last = self.first
		else:
			self.last.next = var
			self.last = var
		return self.size += 1

	def dequeue(self):
		if self.size == 0:
			return False
		temp = self.first
		if self.size == 1:
			self.last = None
		self.first = temp.next
		self.size -= 1
		return temp



#Insertion O(1)
#Removal O(1)
#Searching O(n)
#Access O(n)





stack = []

stack.append(5)
stack.append(8)
stack.append(18)

stack.pop()
stack.pop()

#Stack is just a way of implementing the strucutre in such a way
#that uses LIFO :last in first out
#Generally, there're 2 variations: python(append and pop) & JS(push and pop) and 
#python(insert in the beginning and pop in the beginning) & JS(shift and unshift)



#in our Stack Class we opted for shift and unshift disguised 
#in push and pop. I.e. we'll add and remove from beginning 
#rahter than end as it is O(1) rather than O(n) in Singly Linked List
#Because with append and pop we are to loop till the end
#of the list. [!!!It's Singly Linked List]



class Node:

	def __init__(self,val):
		self.val = val
		self.next = None

class Stack:

	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def push(self,var):
		var = Node(var)
		if not self.first:
			self.first = var
			self.last = self.first
		else:
			temp = self.first
			self.first = var
			var.next = temp #self.first.next = temp

			#another method
			var.next = self.first
			self.first = var
		return self.length += 1
		

	def pop(self,var):
		if self.length == 0:
			return False	
		temp = self.first
		self.first = temp.next
		self.length -= 1
		if self.length == 0:
			self.first = None
			self.last = None
		return temp.val

		#another variant
		temp = self.first
		if self.length == 1: #if self.first == self.last
			self.last = None
		self.first = temp.next
		self.length -= 1
		return temp.val

		#method which also can be used
		temp = self.first
		if self.first == self.last:
			self.first == None
			self.last == None
		else:
			self.first = temp.next
		return temp.val


#Insertion O(1)
#Removal O(1)
#Searching O(n)
#Access O(n)
















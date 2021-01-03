#Big O
#Insertion O(1)
#Removal O(1)
#Searching O(n) technically it's O(n/2) as we use divide and conquer
#access O(n)



class Node:

	def __init__(self,val):
		self.val = val
		self.next = None
		self.prev = None


class DoublyLinked:

	def _init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self,var):
		new = Node(var)
		if not self.head:
			self.head = new
			self.tail = self.head
		else:
			self.tail.next = new
			self.tail.next.prev = self.tail #or new.prev = self.tail
			self.tail = new
		self.length += 1
		return self

	def pop(self):
		if not self.head:
			return False
		temp = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.tail = temp.prev
			self.tail.next = None
			temp.prev = None
		self.length -= 1
		return temp

	def shift(self):
		if not self.head:
			return False
		old = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = old.next
			self.head.prev = None
			old.next = None
		self.length -= 1
		return old

	def unshift(self,var):
		new = Node(var)
		if not self.head:
			self.head = new
			self.tail = self.head
		else:
			new.next = self.head
			self.head.prev = new
			self.head = new
		self.length += 1
		return self

	def get(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		elif ind <= (self.length/2):
			count = 0
			temp = self.head
			while count != ind:
				count += 1
				temp = temp.next
		else:
			count = self.length - 1
			temp = self.tail
			while count != ind:
				count -= 1
				temp = temp.prev
		return temp

	def set(self,ind,var):
		new = self.get(ind)
		if not new:
			return False
		new.val = var
		return True

#actually self.length in two elif statements gets increased as we call those methods
	def insert(self,ind,var):
		if ind < 0 or ind > self.length:
			return False
		elif ind == 0:
			return not self.unshift(var)
		elif ind == self.legnth:
			return not self.push(var)
		else:
			new = Node(var)
			before = self.get(ind - 1)
			after = before.next

			before.next = new
			new.prev = before
			new.next = after
			after.prev = new
			self.length += 1
			return True

	def remove(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		elif ind == 0:
			return self.shift()
		elif ind == self.length - 1:
			return self.pop()
		else:	
			current = self.get(ind)
			current.prev.next = current.next
			current.next.prev = current.prev
			current.prev = None
			current.next = None
			self.length -= 1
			return current

			#with variables
			previous = current.prev
			after = current.next
			previous.next = after
			after.prev = before
			current.next = None
			current.previous = None

		
#Exercises
class Node:

	def __init__(self,val):
		self.val = val
		self.next = None
		self.prev = None

class DoublyOnceMore:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self,var):
		var = Node(var)
		if not self.head:
			self.head = var
			self.tail = self.head
		else:
			self.tail.next = var
			var.prev = self.tail
			self.tail = var
		self.length += 1
		return self

	def unshift(self,var):
		var = Node(var)
		if not self.head:
			self.head = var
			self.tail = self.head
		else:
			self.head.prev = var
			var.next = self.head
			self.head = var
		self.length += 1
		return self

	def shift(self):
		if self.length == 0:
			return False
		temp = self.head
		self.head = temp.next
		self.head.prev = None
		self.length -= 1
		if self.length == 0:
			self.head = None
			self.tail = None
		return temp

		#or more effective one
		if not self.head:
			return False
		elif self.length == 1:
			self.head = None
			self.tail = None
			self.length -= 1
		else:
			temp = self.head
			self.head = temp.next
			self.head.prev = None
			self.length -= 1
			return temp

	def set(self,ind,var):
		if ind < 0 or ind >= self.length:
			return False
		#get part
		var = Node(var)
		if ind <= self.length/2:
			temp = self.head
			count = 0
			while count != ind:
				count += 1
				temp = temp.next
		else:
			temp = self.tail
			count = self.length - 1
			while count != ind:
				count -= 1
				temp = temp.prev
		#set part
		temp.val = var
		return True

		#or we can substitute it with concise:
		temp = self.get(ind)
		if not temp:
			return False
		temp.val = var

	def remove(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		elif ind == 0:
			return self.shift()
		elif ind == self.length - 1:
			return self.pop()
		else:
			current = self.get(ind)
			current.prev.next = current.next
			current.next.prev = current.prev
			current.next = None
			current.prev = None
			self.length -= 1
			return current

			#with variables
			after = current.next
			before = current.prev
			after.prev = before
			before.next = after
			current.next = None
			current.prev = None



	def get(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		elif ind > self.length/2:
			count = self.length - 1
			temp = self.tail
			while count != ind:
				count -= 1
				temp = temp.prev
		else:
			count = 0
			temp = self.head
			while count != ind:
				count += 1
				temp = temp.next
		return temp


	def pop(self):
		if not self.head:
			return False
		elif self.length == 1:
			self.head = None
			self.tail = None
		else:
			temp = self.tail
			self.tail = temp.prev
			self.tail.next = None
			temp.prev = None
		self.length -= 1
		return temp

	def insert(self,ind,var):
		if ind < 0 or ind > self.length:
			return False
		elif ind == 0:
			return not self.unshift(var)
		elif ind == self.length:
			return not self.push(var)
		else:
			current = Node(var)
			before = self.get(ind - 1)
			after = before.next

			before.next = current
			current.prev = before

			after.prev = current
			current.next = after

			self.length += 1
			return True


	def reverse(self):
		curr = self.head
		if curr.next == None or curr == None:
			return False
		while curr != None:
			temp = curr.prev
			curr.prev = curr.next
			curr.next = temp
			curr = curr.prev
		if temp != None:
			temp = temp.prev
		self.head = temp


		#from Leetcode
		lst = self.head
		newHead = None
		while lst != None:
			temp = lst.next
			lst.next = lst.prev
			lst.prev = temp

			if temp == None:
				newHead = lst

			lst = temp
		return self


new = DoublyOnceMore()

new.push(5)
new.push(7)
new.push(9)
new.push(19)
new.push(1)

new.reverse()












































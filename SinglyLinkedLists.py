#piece of data - val
#reference to next node - next

#Big O
#Insertion O(1)
#Removal - It depends: O(1) if the beginning(best case) or O(N) from the end (worst case)
#Searching O(n)
#Access O(n)




class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

# first = Node('Hi')
# first.next = Node('there')
# first.next.next = Node('how')
# first.next.next.next = Node('are')
# first.next.next.next.next = node('you')

#every Node is a new connection => maybe that's why every new value will have it's 
#own .next value. I.e. we have 4 and it's .next is 7. Then we have 7 which .next is 10


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0



	def push(self,new):
		var = Node(new)
		if not self.head:
			self.head = var
			self.tail = self.head
		else:
			self.tail.next = var
			self.tail = var
		self.length += 1
		return self

	@property
	def pop(self):
		if not self.head:
			return None
		nxt = self.head
		cur = nxt
		while nxt.next:
			cur = nxt
			nxt = nxt.next
		self.tail = cur
		self.tail.next = None
		self.length -= 1
		if self.length == 0:
			self.head = None
			self.tail = None
		return cur 

	def shift(self):
		if not self.head:
			return None
		cur = self.head
		self.head = cur.next
		self.length -= 1
		if self.length == 0:
			self.tail = None
		return cur

	def unshift(self,var):
		temp = Node(var)
		if not self.head:
			self.head = temp
			self.tail = self.head
		else:
			temp.next = self.head
			self.head = temp 
		self.length += 1
		return self
	# var.next = self.head
	# self.head = var

	def got(self,ind):
		if ind < 0 or ind >= self.length:
			return None
		count = 0
		pos = self.head
		while pos:
			count += 1
			if count == ind:
				return pos
			pos = pos.next

		#more optimal implementation
		count = 0
		while count != ind:
			pos = pos.next
			count += 1
		return pos

	def set(self,ind,var):
		x = self.got(ind)
		if not x:
			return False
		x.val = var
		return True

	def insert(self,ind,var):
		if ind < 0 or ind > self.length:
			return False	
		elif ind == self.length:
			return not self.push(var)
		elif ind == 0:
			return not self.unshift(var)
		else:
			new = Node(var)	
			x = self.got(ind - 1)
			temp = x.next
			x.next = var
			var.next = temp
			self.length += 1
			return True

		# new.next = x.next
		# x.next = new

	def remove(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		elif ind == self.length - 1:
			return self.pop()
		elif ind == 0:
			return self.shift()
		else:
			index = self.got(ind - 1)
			temp_1 = index.next
			temp_2 = temp_1.next
			index.next = temp_2

			#####more optimal
			index = self.got(ind - 1)
			temp = index.next
			index.next = temp.next
			####
			self.length -= 1
			return temp

	def reverse(self):
		node = self.head
		self.head = self.tail
		self.tail = node
		prev = None
		next_ = None
		i = 0
		while i < self.length:
			next_ = node.next #save next
			node.next = prev #reverse. Here we switch the pointer to self.tail -> None
							#we just reassign the varibale: node.next from now means previous
						# + for the first iteration we have node = 100 => the next of it will
						#be None
						#in other words:
						#we save the next value of the old list
						#and then the next will be the previous
			prev = node  #these two propel prev & node
			node = next_ #and here node means next_ value from above
						#	=> node.next in the upcoming iteratiion will give
						#NOT THE PREVIOUS, but following 
			i += 1
		return self



		


lst = SinglyLinkedList()

lst.push(4)
lst.push(6)
lst.push(8)
print(lst.shift())



##
class Node:

	def __init__(self,val):
		self.val = val
		self.next = None

class SingleList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self,val):
		var = Node(val)
		if not self.head:
			self.head = var
			self.tail = self.head
		else:
			self.tail.next = var
			self.tail = var
		self.length += 1
		return self

	def pop(self):
		if not self.head:
			return False
		temp = self.head
		cur = temp
		while temp:
			cur = temp
			temp = temp.next
		self.tail = cur
		self.tail.next = None
		self.length -= 1
		if self.length == 0:
			self.head = None
			self.tail = None
		return temp

	def shift(self):
		if not self.head:
			return False
		temp = self.head
		self.head = self.head.next #or temp.next
		self.length -= 1
		if self.length == 0:
			self.tail = None
		return temp

	def unshift(self,var):
		new = Node(var)
		if not self.head:
			self.head = new
			self.tail = self.head
		else:
			temp = self.head
			self.head = new
			new.next = temp

			#below Colt's one
			new.next = self.head
			self.head = new
		self.length += 1
		return self

	def get(self,ind):
		if ind < 0 or ind >= self.length:
			return False
		count = 0
		temp = self.head
		while count != ind:
			count += 1
			temp = temp.next
		return temp

	#in set we receive 'x' which is actually value itself,
	#so we don't need to use self on it, but x.val to alter the 'inner value'
	def set(self,ind,var):
		x = self.get(ind)
		if not x:
			return False
		x.val = var
		return True

	def insert(self,ind,var):
		if ind < 0 or ind > self.length:
			return False
		elif ind == 0:
			return not self.unshift(var)
		elif ind == self.length:
			return not self.push(var)
		else:
			new = Node(var)
			temp = self.get(ind - 1)
			temp2 = temp.next
			temp.next = new
			new.next = temp
			self.length += 1
			return True

		def remove(self,ind):
			if ind < 0 or ind > self.length:
				return False
			elif ind == 0:
				return self.shift()
			elif ind == self.length:
				return self.pop()
			else:
				old = self.get(ind - 1)
				temp = old.next
				old.next = temp.next
				self.length -= 1
				return old

		def reverse(self):
			node = self.head
			self.head = self.tail
			self.tail = node
			next_ = None
			prev = None
			i = 0
			while i < self.length:
				next_ = node.next
				node.next = prev
				prev = node
				node = next_
				i += 1
			return self


			


























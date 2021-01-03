#root - the top node in a tree
#child - a node directly connected to another node 
#when moving away from the Root
#Parent - the converse notion of a child
#Siblings - a group of nodes with the same parent
#Leaf - a node with no children
#Edge - the connection between one node and another

#Trees -> Binary Trees -> Binary Search Trees
#Tree can have multiple nodes with undefined amount of children
#Binary Tree: each node at most can have 2 children
#Binary Search Tree can have from 0 to 2 children per node
#and sorted in a binary search manner
#i.e. every node to the left of a parent node is 
#always less than the parent and every node to the
#right of a parent node is always greater than the parent

#Big(O)
#Insertion O(log n)
#Searching O(log n)
#But not guaranteed!!!!
#y = log[2] (x) 
#in other words: only one step up when we 
#DOUBLE the number of nodes
#2x number of nodes: 1 extra step
#4x number of nodes: 2 extra steps
#8x number of nodes: 3 extra steps




class Node:

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None


#every 'tree' variable defines a separate tree. So, we put all values inside one tree
#=> every Node variable has it's own .left and .rigth.
#when there is no root out 'insert' value become .root
#after it next 'insert' at first ALSO defines as Node
#and we compare it with self.root.rigth and self.root.left (instead of self.root we have curr)
#and thus we change values via .right/.left
#the next var is attached to self.root [.left and .right precisely] and 
#so on

class BinarySearchTree:
	
	def __init__(self):
		self.root = None

	#iterative
	def insert(self,var):
		new = Node(var)
		if not self.root:
			self.root = new
			return self
		curr = self.root
		while True:
			if new.value == curr.value:
				return False
			if new.value < curr.value:
				if curr.left == None:
					curr.left = new
					return self
				curr = curr.left
			elif new.value > curr.value:
				if curr.right == None:
					curr.right = new
					return self
				curr = curr.right

	def find_also(self,val):
		if self.root == None:
			return False
		current = self.root
		start = False
		while current and not start:
			#when current hit the end of the tree the loop will stop
			#or when start == True i.e. we found our value
			if val < current.val:
				current = current.left
			elif val > current.val:
				current = current.right
			else: 
				start = True

		if not start: #if start == False then we hitted end of the tree
			return False
		return current

	#resembles the one above, but return only True/False
	def find_tf(self,val):
		if not self.root:
			return False
		cur = self.root
		found = False
		while cur and not found:
			if cur.val > val:
				cur = cur.left
			elif cur.val < val:
				cur = cur.right
			else:
				return True

		return False


		#recursive
##########
class Node(object):

	def __init__(self,data):
		self.root = data
		self.left = None
		self.right = None

class BST(object):

	def __init__(self):
		self.top = None

	def recursive(self,node,data): #node defines root(node) and self.top.root == .val
		if node is None: #if there is no self.top == root
		#we define in BST as self.top, but the all inner stuff (.root, .left, .rigth) defines in Node
		#and all the work in regard to comparision is made because of it
		#one root and if it is != None then
		#newly created node will move either to left or right from it and so on
			node = Node(data)
		elif self.top.root > data: #can we use node.root?
			node.left = self.recursive(node.left,data)
		elif self.top.root < data:
			node.right = self.recursive(node.right,data)

		return node

	def insert(self,data):
		self.top = self.recursive(self.top,data)

conv = BST()
conv.insert(4)
conv.insert(8)
conv.insert(2)
##############
					



tree = BinarySearchTree()
tree.root = Node(10)

#it's aggrieving to make the belowwritten way
#that's why insert method will be implemented
# tree.root.right = Node(15)
# tree.root.left = Node(7)
# tree.root.left.right = Node(9)





##from YouTube

class Node:

	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

class BST:

	def __init__(self):
		self.root = None

	def insert(self,val):
		if not self.root:
			self.root = Node(val)
		else:
			self._insert(val,self.root)

	def _insert(self,var,curr):
		if var < curr.value:
			if curr.left == None:
				curr.left = Node(var)
			else:
				curr = self._insert(var,curr.left)
		elif var > curr.right:
			if curr.right == None:
				curr.right = Node(var)
			else:
				curr = self._insert(var,curr.right)
		else:
			print("Value is already there!")

	def print_tree(self):
		if self.root != None:
			self._tree(self.root)

	def _tree(self,current):
		self._tree(current.left)
		print(str(current.value))
		self._tree(current.right)





















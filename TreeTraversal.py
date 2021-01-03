
class Node:

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class Tree:

	def __init__(self):
		self.root = None

	def insert(self,var):
		new = Node(var)
		if not self.root:
			self.root = new
			return self
		curr = self.root
		while True:
			if curr.value > new.value:
				if curr.left == None:
					curr.left = new
					return self
				curr = curr.left
			elif curr.value < new.value:
				if curr.right == None:
					curr.right = new
					return self
				curr = curr.right


#BFS
	def bfs_traverse(self):
		node = self.root
		queue, stored = [node], []
		while len(queue) != 0:
			node = queue.pop(0)
			stored.append(node)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		return stored

#DFS
	def dfs_PreOrder(self):
		explored = []
		current = self.root
		def traverse(node):
			explored.append(node)
			if node.left:
				traverse(node.left)
			if node.right:
				traverse(node.right)
		traverse(current)
		return explored

	def dfs_PostOrder(self):
		node = self.root
		stored = list()
		def traverse(node):
			if node.left:
				traverse(node.left)
			if node.right:
				traverse(node.right)
			stored.append(node.value)
		traverse(node)
		return stored

	def dfs_InOrder(self):
		result = list()
		root = self.root
		def traverse(node):
			if node.left:
				traverse(node.left)
			result.append(node.value)
			if node.right:
				traverse(node.right)
		traverse(root)
		print(result)
		return result


tree = Tree()
tree.insert(7)
tree.insert(8)
tree.insert(10)
tree.insert(1)
tree.insert(5)
tree.dfs_InOrder()


























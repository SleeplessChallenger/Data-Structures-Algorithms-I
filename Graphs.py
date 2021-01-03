
#Vertex - a node
#Edge - connection between nodes
#Weighted/Unweighted - values assigned to distances between vertices
#Directed/Undirected - directions assigned to distance between vertices
#i.e. undirected means the edge has arrows in two directions <->
#while directed one means the arrow points only in one direction ->/<-
#It's connected with traverse action
#Weighted means edges have values on them and in unweighted there are plain connections


#Adjacency matrix & adjacency list
#Matrix in general takes up more space, especially in sparse datasets
#+ iteration is slower, but search is faster
#If data is very packed then matrix is better, but more often in real
#world list is used
#List takes up less space, faster to iterate, but search can be slower


class Graph:

	def __init__(self):
		self.adjacencyList = {}

	def addVertex(self,vert):
		if vert in self.adjacencyList:
			return False
		self.adjacencyList[vert] = []

	def addEdge(self,vert1,vert2):
		self.adjacencyList[vert1] += [vert2]
		self.adjacencyList[vert2] += [vert1]
		
	def removeEdge(self,vert1,vert2):
		self.adjacencyList[vert1].remove(vert2)
		self.adjacencyList[vert2].remove(vert1)

	def removeVertex(self,vert):
		for x in self.adjacencyList.keys():
			if x != vert and vert in self.adjacencyList[x]:
				self.removeEdge(x,vert)
		del self.adjacencyList[vert]
		print(self.adjacencyList)


	#DFS

	def dfs_recur(self,vert):
		spit = list()
		explored = dict()
		def dfs(vertex):
			if vertex:
				spit.append(vertex)
				explored[vertex] = True
				for x in self.adjacencyList[vertex]:
					if x not in explored:
						dfs(x)
			return 
		dfs(vert)
		print(spit)
		return spit

# ['A', 'B', 'D', 'E', 'C', 'F']

	def dfs_iter(self,vert):
		stack = [vert]
		result = []
		explored = dict()
		explored[vert] = True
		while len(stack) != 0:
			node = stack.pop()
			result.append(node)
			for x in self.adjacencyList[node]:
				if x not in explored:
					explored[x] = True
					stack.append(x)
		print(result)
		return result

# ['A', 'C', 'E', 'F', 'D', 'B']

	def bfs(self,vert):
		queue = [vert]
		result = []
		explored = {}
		explored[vert] = True
		while len(queue) != 0:
			node = queue.pop(0)
			result.append(node)
			for x in self.adjacencyList[node]:
				if x not in explored:
					explored[x] = True
					queue.append(x)
		print(result)
		return result

#['A', 'B', 'C', 'D', 'E', 'F']


gr = Graph()

gr.addVertex('A')
gr.addVertex('B')
gr.addVertex('C')
gr.addVertex('D')
gr.addVertex('E')
gr.addVertex('F')	

gr.addEdge('A','B')
gr.addEdge('A','C')
gr.addEdge('B','D')
gr.addEdge('C','E')
gr.addEdge('D','E')
gr.addEdge('D','F')
gr.addEdge('E','F')

# gr.dfs_recur('A')
# gr.dfs_iter('A')
gr.bfs('A')

# gr.addVertex('Tokyo')
# gr.addVertex('Osaka')
# gr.addVertex('Fukuoka')
# gr.addVertex('Nagasaki')

# gr.addEdge('Osaka','Tokyo')
# gr.addEdge('Tokyo','Nagasaki')
# gr.addEdge('Fukuoka','Nagasaki')


# gr.dfs_recur('Osaka')



























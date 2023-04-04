"""
Vertex - a node
Edge - connection between nodes
Weighted/Unweighted - values assigned to distances between vertices
Directed/Undirected - directions assigned to distance between vertices
i.e. undirected means the edge has arrows in two directions <->
while directed one means the arrow points only in one direction ->/<-
It's connected with traverse action
Weighted means edges have values on them and in unweighted there are plain connections

Adjacency matrix & adjacency list
* Matrix in general takes up more space, especially in sparse datasets
+ iteration is slower, but search is faster

* If data is very packed then matrix is better, but more often in real
world list is used
* List takes up less space, faster to iterate, but search can be slower
"""


class Graph:

    def __init__(self):
        self.adjacencyList = {}

    def add_vertex(self, vert):
        if vert in self.adjacencyList:
            return False
        self.adjacencyList[vert] = []

    def add_edge(self, vert1, vert2):
        self.adjacencyList[vert1] += [vert2]
        self.adjacencyList[vert2] += [vert1]

    def remove_edge(self, vert1, vert2):
        self.adjacencyList[vert1].remove(vert2)
        self.adjacencyList[vert2].remove(vert1)

    def remove_vertex(self, vert):
        for x in self.adjacencyList.keys():
            if x != vert and vert in self.adjacencyList[x]:
                self.remove_edge(x, vert)
        del self.adjacencyList[vert]
        print(self.adjacencyList)

    # DFS
    def dfs_recur(self, vert):
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

    def dfs_iter(self, vert):
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

    def bfs(self, vert):
        queue = [vert]
        result = []
        explored = {vert: True}
        while len(queue) != 0:
            node = queue.pop(0)
            result.append(node)
            for x in self.adjacencyList[node]:
                if x not in explored:
                    explored[x] = True
                    queue.append(x)
        print(result)
        return result


if __name__ == "__main__":
    gr = Graph()

    gr.add_vertex('A')
    gr.add_vertex('B')
    gr.add_vertex('C')
    gr.add_vertex('D')
    gr.add_vertex('E')
    gr.add_vertex('F')

    gr.add_edge('A', 'B')
    gr.add_edge('A', 'C')
    gr.add_edge('B', 'D')
    gr.add_edge('C', 'E')
    gr.add_edge('D', 'E')
    gr.add_edge('D', 'F')
    gr.add_edge('E', 'F')

    gr.dfs_recur('A')
    gr.dfs_iter('A')
    gr.bfs('A')

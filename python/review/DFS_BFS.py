class Node:
	def __init__(self, data):
		self.data = data
		self.adjacent = []
		self.distance = []
		self.visited = False

	def add_adjacent(self, adj, dist):
		self.adjacent.append(adj)
		self.distance.append(dist)

## just traversal
def DFS(node):
	stack = [node]
	while stack:
		v = stack.pop()
		v.visited = True
		for neighbor in node.adjacent:
			if neighbor.visited = False:
				stack.append(child)

	return None

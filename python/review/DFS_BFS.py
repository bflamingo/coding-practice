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
		for neighbor in v.adjacent:
			if neighbor.visited is False:
				stack.append(neighbor)

	return None

from collections import deque
def BFS(node):
	queue = deque()
	queue.append(node)
	while queue:
		v = queue.popleft()
		v.visited = True
		for neighbor in v.adjacent:
			if neighbor.visited is False:
				queue.append(neighbor)

	return None


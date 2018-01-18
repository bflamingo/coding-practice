from collections import deque ## for queue implementation in BFS.
import unittest
import math ## for inf.

class Node:
	def __init__(self, data):
		self.data = data
		self.adjacent = []
		self.distance = {}

	def add_adjacent(self, adj, dist):
		self.adjacent.append(adj)
		self.distance[adj] = dist

## just traversal
def DFS(node):
	stack = [node]
	visited = {}
	while stack:
		v = stack.pop()
		visited[v] = True
		for neighbor in v.adjacent:
			if visited[neighbor] is False:
				stack.append(neighbor)

	return None


def BFS(node):
	queue = deque()
	queue.append(node)
	visited = {}
	while queue:
		v = queue.popleft()
		visited[v] = True
		for neighbor in v.adjacent:
			if visited[v] is False:
				queue.append(neighbor)

	return None


## Node discovery
def DFS_discover(node):
	stack = [node]
	visited = {}
	all_nodes = []
	while stack:
		v = stack.pop()
		visited[v] = True
		all_nodes.append(v)
		for neighbor in v.adjacent:
			if visited[neighbor] is False:
				stack.append(neighbor)

	return all_nodes


def BFS_discover(node):
	queue = deque()
	queue.append(node)
	visited = {}
	all_nodes = []
	while queue:
		v = queue.popleft()
		visited[v] = True
		all_nodes.append(v)
		for neighbor in v.adjacent:
			if visited[v] is False:
				queue.append(neighbor)

	return all_nodes



# Dijkstra's
def dijkstra(source):
	distance = {}
	parent = {}
	
	# Populate vertex set using BFS/DFS node discovery
	vertex_set = BFS_discover(source)

	# Initialize distance estimates and parent map
	for vertex in vertex_set:
		distance[vertex] = math.inf
		parent[vertex] = None
	distance[source] = 0

	while vertex_set:
		# Extract minimum dist node from vertex set, ties broken arbitrarily
		min_dist = min(vertex_set.values())
		for node in vertex_set:
			if distance[node] == min_dist:
				current = node
				vertex_set.remove(node)
				break

		for neighbor in current.adjacent:
			if neighbor in vertex_set:
				estimate = dist[current] + current.distance[neighbor]
				if estimate < distance[neighbor]:
					dist[neighbor] = estimate
					parent[neighbor] = current

	return distance, parent






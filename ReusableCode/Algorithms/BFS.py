# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# Function to find the shortest path
	def BFS_Path(self, start, value):
		queue = []
		visited = []

		queue.append([start,[start]])

		while queue:
			print(queue)
			curr = queue.pop(0)
			visited.append(curr[0])
			if curr[0] == value:
				return curr[1]
			else:
				for i in self.graph[curr[0]]:
					if i not in visited:
						queue.append([i, curr[1] + [i]])


			


	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True
		traverse = ''
		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			traverse += str(s) + ' '

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
		print(traverse)

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# print ("Following is Breadth First Traversal"
# 				" (starting from vertex 2)")
# g.BFS(2)
print(g.BFS_Path(0,3))

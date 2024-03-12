from collections import defaultdict
class Graph:

        # Constructor
        def __init__(self):

            # default dictionary to store graph
            self.graph = defaultdict(list)

        # function to add an edge to graph
        def addEdge(self, u, v):
            self.graph[u].append(v)

        # A function used by DFS
        def DFSUtil(self, v, target, visited,i,arr):
            if v == target:
                arr.append(i - 1)
                print(arr)

            # Mark the current node as visited
            # and print it
            visited.add(v)

            # Recur for all the vertices
            # adjacent to this vertex
            for neighbour in self.graph[v]: 
                if neighbour not in visited:
                    self.DFSUtil(neighbour, target, visited,i + 1,arr)

        # The function to do DFS traversal. It uses
        # recursive DFSUtil()
        def DFS(self, v, target):

            # Create a set to store visited vertices
            visited = set()

            # Call the recursive helper function
            # to print DFS traversal
            ans = self.DFSUtil(v, target, visited,0,[])

t = int(input())
for _ in range(t):
    nm = list(map(int,input().rstrip().split()))
    n, m = nm[0], nm[1]

    g = Graph()
    for _ in range(m):
        uvc = list(map(int,input().rstrip().split()))
        u, v, c = uvc[0], uvc[1], uvc[2]
        g.addEdge(u, v)
        g.addEdge(v, u)

    be = list(map(int,input().rstrip().split()))
    b, e = be[0], be[1]
    if b == e:
        print(f'Ans: {0}')
    else:
        g.DFS(b,e)

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def bfs(self,source):
        bfs = []
        visited = [False]*self.V
        queue = [source]
        visited[source] = True
        while queue:
            s = queue.pop(0)
            bfs.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
        return bfs
            
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        
    
    def edges(self):
        return (self.graph)
    

V = 4
g = Graph(V)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.bfs(0))
print(g.edges())


# OUTPUT
# [0, 1, 2, 3]
# defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})

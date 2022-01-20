from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    
    def dfsUtil(self,src,visited,a):
        visited[src] = True
        a.append(src)
        for i in self.graph[src]:
            if visited[i] == False:
                self.dfsUtil(i,visited,a)
    
    def dfs(self,src):
        visited = [False]*self.V
        a = []
        self.dfsUtil(src,visited,a)
        return a
            
    
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
print(g.edges())
print(g.dfs(2))




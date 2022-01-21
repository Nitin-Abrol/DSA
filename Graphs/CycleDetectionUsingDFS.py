from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        
    
    def edges(self):
        return (self.graph)
    
    def isCyclicByDFS(self,vertex,parent,visited):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                if self.isCyclicByDFS(neighbour,vertex,visited):
                    return True
            elif neighbour != parent:
                return True
        
        return False
        
    
    def cyclicCheckDFS(self):
        visited = [False]*self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.isCyclicByDFS(i,-1,visited):
                    return True
        return False
    

V = 4
g = Graph(V)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.edges())
print(g.cyclicCheckDFS())

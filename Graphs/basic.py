from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)      
            
    #This example is for undirected graph.
    #Remove the 2nd if condition in case of Directed graph.
    
    def addEdge(self, src, dest):
        if dest not in self.graph[src]:             
            self.graph[src].append(dest)
        if src not in self.graph[dest]: 
            self.graph[dest].append(src)
        
    
    def edges(self):
        return (self.graph)
    
if __name__ == "__main__":
    noOfVertices = 4
    g = Graph(noOfVertices)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.edges())

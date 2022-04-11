from collections import defaultdict


class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,src,dest):
        self.graph[src].append(dest)
       
    def egdes(self):
        print(self.graph)
        
    def bfs_color(self,node,color):
        q = [node]
        color[node] = 1
        while q:
            n1 = q.pop(0)
            for i in self.graph[n1]:
                if color[i] == -1:
                    color[i] = 1 - color[n1]
                    q.append(i)
                elif color[i] == color[n1]:
                    return False
        return True
                     
        
    def bipartite_graph_bfs(self):
        color = [-1]*(self.vertices+1)
        for i in range(1,self.vertices+1):
            if color[i] == -1:
                if not self.bfs_color(i,color):
                    return False
        return True

if __name__ =='__main__':
    g = Graph(6)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(4,6)
    g.addEdge(5,6)
    g.egdes()
    print(g.bipartite_graph_bfs())
    
    
    
    
# OUTPUT
# defaultdict(<class 'list'>, {1: [2], 2: [3], 3: [4], 4: [5, 6], 5: [6]})
# False

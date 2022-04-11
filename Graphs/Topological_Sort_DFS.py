# Uses STACK

from collections import defaultdict

class Graph_directed:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,src,dst):
        if dst not in self.graph[src]:
            self.graph[src].append(dst)
    
    def edges(self):
        print(self.graph)
        
    def topo_sort_dfs(self,node,visited,s):
        visited[node] = 1
        for i in self.graph[node]:
            if not visited[i] :
                self.topo_sort_dfs(i,visited,s)
        s.append(node)
        
    def dfs_topo_sort(self):
        visited = [0]*(self.vertices+1)
        s = []
        for i in range(1,self.vertices+1):
            if not visited[i]:
                self.topo_sort_dfs(i,visited,s)
        
        print(s[::-1])
    
if __name__ == '__main__':
    g = Graph_directed(5)
    g.addEdge(4,0)
    g.addEdge(5,0)
    g.addEdge(3,1)
    g.addEdge(4,1)
    g.addEdge(5,2)
    g.addEdge(2,3)
    g.dfs_topo_sort()
    
    
# OUTPUT
# [5, 4, 0, 2, 3, 1]

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
        
    def indegree(self):
        indegree = [0]*(self.vertices+1)
        for i in range(1,self.vertices+1):
            for node in self.graph[i]:
                indegree[node]+=1
        return indegree

    def topo_sort_bfs(self):
        indegree = self.indegree()
        q = [i for i in range(len(indegree)) if indegree[i]==0]
        
        topo = []
        while q:
            node = q.pop()
            topo.append(node)
            for i in self.graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return topo
    
if __name__ == '__main__':
    g = Graph_directed(5)
    g.addEdge(4,0)
    g.addEdge(5,0)
    g.addEdge(3,1)
    g.addEdge(4,1)
    g.addEdge(5,2)
    g.addEdge(2,3)
    g.edges()
    print(g.topo_sort_bfs())
    
    

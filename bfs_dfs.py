#Breath First Traversal (BFS)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

#Depth First Traversal (DFS)

class Graph2:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFUtil(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFUtil(i, visited)
    def DFS(self,v):
        visited=[False]*(len(self.graph))
        self.DFUtil(v,visited)

#Disjoint Set/Union-Find

class Graph3:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def find_parent(self,parent,i):
        if parent[i]==-1:
            return(i)
        if parent[i]!=-1:
            return(self.find_parent(parent,parent[i]))
    def union(self,parent,x,y):
        x_set=self.find_parent(parent,x)
        y_set=self.find_parent(parent,y)
        parent[x_set]=y_set
    def isCyclic(self):
        parent=[-1]*(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                x=self.find_parent(parent,i)
                y=self.find_parent(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)

#Euler's totient function
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def phi(a):
    if a==1:
        return 1
    else:
        b=a-1
        c=0
        while b:
            if not gcd(a,b)-1:
                c+=1
            b-=1
        return c

#Fermat's method
def Fermat(n):
    return (2<<n-2)%n==1

gg = Graph2()
gg.addEdge(0, 1)
gg.addEdge(0, 2)
gg.addEdge(1, 2)
gg.addEdge(2, 0)
gg.addEdge(2, 3)
gg.addEdge(3, 3)

g = Graph3(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
 
if g.isCyclic():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle")

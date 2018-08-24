class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = 0          # color of the vertex (white, gray, and black)
        self.d = 1000           # depth
        self.p = None           # parent
        self.adj = list()       # adjacency list
        self.t1 = 0             # time entered
        self.t2 = 0             # time exit

    def __str__(self):
        return str(self.key) + ":" + str(self.t1) + '--' + str(self.t2)

class Graph:
    time = 0

    def __init__(self, verts):
        self.s = None
        self.build(verts)

    def build(self, v):
        L = [None] * len(v)
        for i in range(len(v)):
            L[i] = Vertex(i)
        for i in range(len(v)):
            for n in v[i]:
                L[i].adj.append(L[n])
        self.s = L

    def bfs(self):
        s = self.s[0]
        s.color = 1
        s.d = 0
        s.p = None
        q = []
        q.append(s)
        while len(q) > 0:
            u = q.pop(0)
            for v in u.adj:
                if v.color == 0:
                    v.color = 1
                    v.d = u.d + 1
                    v.p = u
                    q.append(v)
            u.color = 2

    def printPath(self, s, v):
        if s is v:
            print(s)
        elif v.p is None:
            print('no path')
        else:
            self.printPath(s, v.p)
            print(v)

    def dfs(self):
        def recDfs(u):
            Graph.time += 1
            u.t1 = Graph.time
            u.color = 1
            print('Enters ', u)
            for v in u.adj:
                if v.color == 0:
                    v.p = u
                    recDfs(v)
            u.color = 2
            Graph.time += 1
            u.t2 = Graph.time
            print('Exits ', u)
        for u in self.s:
            if u.color == 0:
                recDfs(u)

if __name__ == '__main__':
    v = [[1,4],[0,2,3,4],[1,3],[1,2,4],[0,1,3]]
    g = Graph(v)
#    g.bfs()
#    g.printPath(g.s[0], g.s[3])
    g.dfs()

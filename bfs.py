def bfs(g, s):
    state = {}
    p = {}
    for v in g:
        if v != s:
            state[v] = "undiscovered"
            p[v] = None
    state[s] = "discovered"
    p[s] = None
    Q = [s]
    while len(Q) != 0:
        u = Q.pop(0)
        print "Processing", u.name
        for v in u.neighbours:
            print u.name + "->" + v.name
            if state[v] == "undiscovered":
                state[v] = "discovered"
                p[v] = u
                Q.append(v)
        state[u] = "processed"


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, v):
        self.neighbours.append(v)

    def __repr__(self):
        return self.name

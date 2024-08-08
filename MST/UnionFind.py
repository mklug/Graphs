class UnionFind:

    def __init__(self, keys):
        self.uf = {k: k for k in keys}

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        ux = self.find(x)
        uy = self.find(y)
        self.uf[ux] = self.uf[uy]

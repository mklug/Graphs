from UnionFind import UnionFind


def kruskal(G, weights):
    '''Returns a list of edges [(u,v),...] in a 
    minimal spanning forest.

    The graph G is a dictionary representing the 
    adjacency list form of a graph.  The weight
    parameter is a dictionary from edge pairs
    to real numbers. 

    Time complexity: 
    O(E log(E)) + O((V+E)alpha(V)) = O((V+E) log(E))
                                   = O((V+E) log(V))
    Space Complexity:
    O(E)
    '''
    edges = []
    for v in G.keys():
        for w in G[w]:
            edges.append((v, w))

    edges.sort(key=lambda x: weights[x])
    uf = UnionFind(edges)
    res = []
    for edge in edges:
        u, v = edge
        if uf.find(u) != uf.find(v):
            res.append(edge)
            uf.union(u, v)
    return res

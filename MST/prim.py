import heapq

# Set-based implementation of Prim.
# O(V(V + E)) time, O(V + E) space


def prim(G, weights):
    '''Takes as input a graph given as an 
    adjacency list (in the form of a dictionary
    with node keys and list of node values) and a 
    dictionary assigning edges to weights. 

    Returns the list of edges in a minimal spanning 
    tree of G.    
    '''

    INF = float("inf")
    d = {v: INF for v in G.keys()}
    Q = set(d.keys())

    def extract_min():
        res = min(Q, key=d.get)
        Q.remove(res)
        return res

    parents = {}
    while len(Q) > 0:
        u = extract_min()
        for v in G[u]:
            if v in Q and weights[(u, v)] < d[v]:
                d[v] = weights[(u, v)]
                parents[v] = u

    edges = []
    for v in parents:
        edges.append((v, parents[v]))
    return edges


# Min-heap implementation of Prim.
# Time O((V + E) * log(V + E) + E) = O((V+E)(log(V)))
# Space O(V + E).


def prim_heap(G, weights):
    '''Takes as input a graph given as an 
    adjacency list (in the form of a dictionary
    with node keys and list of node values) and a 
    dictionary assigning edges to weights. 

    Returns the list of edges in a minimal spanning 
    tree of G.    
    '''

    INF = float("inf")

    d = {v: INF for v in G.keys()}
    h = heapq.heapify([(v, k) for k, v in d.items()])
    seen = set()

    parents = {}
    while len(h) > 0:
        priority, u = heapq.heappop(h)

        # Check if priority changed.
        if d[u] < priority:
            continue

        for v in G[u]:
            weight = weights[(u, v)]
            if v not in seen and weight < d[v]:
                d[v] = weight
                heapq.heappush(h, (weight, v))
                parents[v] = u
        seen.add(u)

    edges = []
    for v in parents:
        edges.append((v, parents[v]))
    return edges

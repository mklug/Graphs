from collections import heapq

# Simplest implementation without a heap.


def dijkstra(G, weights, s):
    '''Finds the distance from s to all vertices
    in the weighted directed graph G (given as
    a dictionary representing the adjacency lists).

    The edge weights must all be non-negative.  
    '''

    INF = float("inf")
    d = {v: INF for v in G.keys()}
    d[s] = 0
    # min_path_tree = {}

    Q = set(d.keys())

    def extract_min(Q):
        res = min(Q, key=d.get)
        Q.remove(res)
        return res

    while len(Q) > 0:
        u = extract_min(Q)
        for v in G[u]:
            relaxed = d[u] + weights[(u, v)]
            if d[v] > relaxed:
                d[v] = relaxed
                # min_path_tree[v] = u

    return d


'''
Notes:

- Time complexity is O(V^2 + E) = O(V^2), space 
  complexity is O(V).

- If the vertices of the graph are numbered 0,1,...,V-1,
  then a list can be used in place of a dictionary for d
  to cut down on lookup cost.  

- If the explicit minimum tree is desired, the only changes
  that must be made are the initialization

        minimum_tree = {} 

  outside of the loop, and the relaxation step should add

        minimum_tree[v] = u    
'''


# Min-heap implementation.
# Time O((V+E)logE) = O((V+E)logV), space O(V + E).

def dijkstra_heap(G, weights, s):
    '''Finds the distance from s to all vertices
    in the weighted directed graph G (given as
    a dictionary representing the adjacency lists).

    The edge weights must all be non-negative.  
    '''

    INF = float("inf")
    d = {v: INF for v in G.keys()}
    d[s] = 0

    # min-heap of tuples
    h = [(0, s)]  # (priority, vertex)

    while len(h) > 0:
        priority, u = heapq.heappop(h)

        # Check if priority has changed.
        if d[u] < priority:
            continue

        for v in G[u]:
            relaxed = d[u] + weights[(u, v)]
            if relaxed < d[v]:
                d[v] = relaxed
                heapq.heappush(h, (relaxed, v))

    return d

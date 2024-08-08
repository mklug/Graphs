def bellman_ford(G, weights, s):
    '''Finds a minimum path tree of the directed 
    graph given as an adjacency dictionary, 
    rooted at s.  

    Returns a tuple of two dictionaries.  

    The first dictionary where the keys are the vertices 
    in the connected component of s and where the values
    are the distances to s.

    The second returned dictionary is the dictionary
    where the keys are the vertices in the connected 
    component of s, the value of s is None and the 
    value of all all keys is a predecessor in a 
    minimum path tree rooted at s.  

    If there is a negative cycle reachable from s, 
    returns a tuple of empty dictionaries.
    '''

    INF = float("inf")

    # Distances to be relaxed.
    d = {v: INF for v in G.keys()}
    d[s] = 0

    min_path_tree = {}
    V = len(G.keys())

    for _ in range(V-1):
        for u in G.keys():
            for v in G[u]:
                relaxed = d[u] + weights[(u, v)]
                if relaxed < d[v]:
                    d[v] = relaxed
                    min_path_tree[v] = u

    # Check for negative cycles.
    for v in G.keys():
        for u in G[v]:
            if d[u] + weights[(u, v)] < d[v]:
                return {}, {}

    return d, min_path_tree

# Variations:
#
# - You may know that there are no negative cycles
#   in which case you can ignore the second for-loop
#   (or use Dijkstra's algorithm).
#
# - You may not need the min path tree, in which
#   case you can remove all the lines involving it.
#
# - You may just want the distance to a sink node
#   t in which case you can just return d[t].
#
# - You might want the returned minimum distance
#   tree edges pointed in the opposite direction.
#   The tree should then be reversed before being
#   returned.
#
# - The input graph might not have a separate
#   weights dictionary but rather have the values
#   be lists of tuples with the neighbor vertices
#   and the weight of the edge.  The code can
#   easily be modified for graphs in that format.
#
# - One potential optimization is to check mark
#   if d has changed in each pass and return if
#   it has not.
#
# - There are other potential optimizations based
#   on ordering the edges in certain ways that
#   decrease the necessary number of passes
#   (e.g., Yen's optimiation).

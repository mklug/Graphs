'''
    Implementation of topological sort using Kahn's 
    algorithm (which I find a bit easier than the DFS-
    based implementation).  The approach is to keep 
    track of the nodes with in-degree zero and remove
    them until there are no more.  This process either
    does not remove all of the nodes (in which case there
    is a cycle) or produces a topological sorting of 
    the graph.  

    This algorithm can be slightly simplified if 
    we can assume that the input is a DAG -- namely,
    by removing the final 'if' statement.

    If all that is desired is a cycle detection 
    algorithm, then the below algorithm can be 
    simplified by removing all references to the 
    returned list and just maintaining a counter
    for the number of nodes remaining.  
    
    Graphs given as adjacency list.  For example:

    G = {0 : [1,2,3],
        1 : [],
        2 : [],
        3 : []}

'''

import collections

# Returns an empty list if the input is not a DAG.
# O(V + E) time, O(V) space.


def top_sort(G):

    in_degree = collections.Counter()
    for v in G.keys():
        for w in G[v]:
            in_degree[w] += 1

    res = []
    in_degree_zero = []  # Can remove in an arbitrary order.
    for v in G.keys():
        if in_degree[v] == 0:
            in_degree_zero.append(v)
            res.append(v)

    while len(in_degree_zero) > 0:

        current = in_degree_zero.pop()
        for w in G[current]:
            in_degree[w] -= 1
            if in_degree[w] == 0:
                in_degree_zero.append(w)
                res.append(w)

    if len(res) != len(G.keys()):
        return []

    return res

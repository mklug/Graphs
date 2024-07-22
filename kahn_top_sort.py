'''
    Implementation of topological sort using Kahn's 
    algorithm (which I find a bit easier than the DFS-
    based implementation).  The approach is to keep 
    track of the nodes with out degree zero and remove
    them until there are no more.  This process either
    does not remove all of the nodes (in which case there
    is a cycle) or removes the nodes in an order that 
    is the reverse of a topological sorting of the graph.  

    Slightly more space is needed for this algorithm
    in comparison to the DFS-based approach to 
    topological sorting since we need to construct 
    the reverse of the input graph.  

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
# O(V + E) time, O(V + E) space.


def top_sort(G):
    G_reverse = collections.defaultdict(set)
    for v in G.keys():
        for w in G[v]:
            G_reverse[w].add(v)

    out_degree = collections.Counter()
    for v in G.keys():
        out_degree[v] += len(G[v])

    res = []
    out_degree_zero = []  # Can remove in an arbitrary order.
    for v in G.keys():
        if out_degree[v] == 0:
            out_degree_zero.append(v)
            res.append(v)

    while len(out_degree_zero) > 0:
        current = out_degree_zero.pop()
        for w in G_reverse[current]:
            out_degree[w] -= 1
            if out_degree[w] == 0:
                out_degree_zero.append(w)
                res.append(w)

    if len(res) != len(G.keys()):
        return []

    return res[::-1]

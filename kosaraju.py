'''
    Kosaraju's algorithm to find the strongly connected
    components of a directed graph.  In fact, it does a 
    bit more and also finds a topological ordering on the 
    strongly connected components of the input graph.  

    A naive algorithm for doing this would do a search
    from eavh pair of vertices to see if they can reach each
    other, thus taking time O((V+E)^2).  Kosaraju's algorithm
    accomplishes this in time O(V+E).
'''

import collections

# Returns the strongly connected components of G in a
# topological ordering.
# O(V + E) time, O(V + E) space.


def kosaraju(G):

    # Do a "DFS topological sorting" of the nodes of G.
    # Of course G might have edges, so this is not a
    # real toplogical sorting.
    node_order = []
    visited = {k: False for k in G.keys()}

    def go(node):
        if visited[node]:
            return
        visited[node] = True
        for x in G[node]:
            go(x)
        node_order.append(node)

    for node in G.keys():
        go(node)
    node_order = node_order[::-1]

    # Reverse the graph.
    G_reverse = collections.defaultdict(set)
    for v in G.keys():
        for w in G[v]:
            G_reverse[w].add(v)

    # Explore the reverse graph in the order given from
    # the "topological sorting".
    seen = {k: False for k in G.keys()}

    # Return list of nodes reachable from the root
    # in the reverse graph of G.
    def reachable(root):
        ans = []

        def dfs(node):
            if seen[node]:
                return
            ans.append(node)
            seen[node] = True
            for v in G_reverse[node]:
                dfs(v)

        dfs(root)
        return ans

    res = []
    for node in node_order:
        if not seen[node]:
            res.append(reachable(node))
    return res

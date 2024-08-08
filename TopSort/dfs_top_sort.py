'''
    Implementation of topological sort and related algorithms 
    using DFS.  In particular, the following problems can
    be solved with only minor modifications to the code:

    (1) Given a directed graph, determine if it has a cycle.  

    (2) Given a directed graph, return a topological 
    ordering of the graph, if the graph is acyclic.  If 
    the graph is contains a cycle, give a return value to 
    indicate this.  

    We warm up by showing how to find a topological ordering 
    on a DAG.  The strategy here is to follow edges in a DFS 
    fashion until you can not anymore, at which point the 
    node are put on a stack.  This stack is then returned in
    reverse order.  

    The same basic idea is how cycle detection is performed,
    except there we need three states which signify if a node
    is in the stack of nodes we have finished processing 
    (BLACK below), if we currently are processing a node on the 
    call stack (GRAY below), or a node has yet to be seen (WHITE
    below).  Cycles appear when we bump into a node currently
    being processed.  

    Finally, we include a function that, using topological 
    sprting, finds the longest path length in a DAG (using bottom
    up dynamic programming).      


    Graphs given as adjacency list.  For example:

    G = {0 : [1,2,3],
        1 : [],
        2 : [],
        3 : []}

    G = {0:[],
        1:[],
        2:[3],
        3:[1],
        4:[0,1],
        5:[2,0]}

    G = {0:[1,2],
        1:[3],
        2:[3],
        3:[]}
'''

# Imput must be a DAG.
# Returns a topological sort of the input.
# O(V + E) time, O(V) space.


def top_sort(G):
    res = []
    visited = {k: False for k in G.keys()}

    def go(node):
        if visited[node]:
            return
        for x in G[node]:
            go(x)
        res.append(node)
        visited[node] = True

    for node in G.keys():
        go(node)
    return res[::-1]


# Cycle detection.
# # O(V + E) time, O(V) space.
def has_cycle(G):
    # WHITE : Never visited.
    # GRAY : Currently in process, not finished.
    # BLACK : Finished.
    WHITE, GRAY, BLACK = 0, 1, 2
    visited = {k: WHITE for k in G.keys()}

    def go(node):
        # Returns False if we find a cycle.
        if visited[node] == GRAY:
            return False
        visited[node] = GRAY
        for x in G[node]:
            if visited[node] == BLACK:
                continue
            if not go(x):
                return False

        visited[node] = BLACK
        return True

    for node in G.keys():
        if visited[node] == WHITE:
            if not go(node):
                return False
    return True


# Returns a topological sorting if possible,
# otherwise, returns a empty list if there is
# a cycle.
# O(V + E) time, O(V) space.
def top_sortable(G):
    res = []
    WHITE, GRAY, BLACK = 0, 1, 2
    visited = {k: WHITE for k in G.keys()}

    def go(node):
        # Returns False if we find a cycle.
        if visited[node] == GRAY:
            return False
        visited[node] = GRAY
        for x in G[node]:
            if visited[node] == BLACK:
                continue
            if not go(x):
                return False
        visited[node] = BLACK
        res.append(node)
        return True

    for node in G.keys():
        if visited[node] == WHITE:
            if not go(node):
                return []
    return res[::-1]


# Given a DAG, returns the length of the
# longest path in G.
# O(V + E) time, O(V) space.
def longest_path_length(G):
    top_order = top_sort(G)
    length_to = {v: 0 for v in G.keys()}
    # Should maybe be 1 -- depends on how you count lengths of paths.
    for v in top_order:
        for neighbor in G[v]:
            length_to[neighbor] = max(length_to[neighbor], length_to[v] + 1)
    return max(length_to.values())

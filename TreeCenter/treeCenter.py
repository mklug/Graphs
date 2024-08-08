
# Simple leaf pruning.
# O(n) time and O(n) space.
def getCenters(N, edges):
    '''
    Gets the center(s) of a tree with N vertices 
    labeled 0,..., N - 1 and given edges.   
    >>> getCenters(2, [[0,1]])
    [0, 1]
    >>> getCenters(4, [[0,1],[0,2],[0,3]])
    [0]
    >>> getCenters(4, [[0,1],[1,2],[2,3]])
    [1, 2]
    '''
    tree = {i: set() for i in range(N)}
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)

    leaves = [i for i in range(N) if len(tree[i]) <= 1]

    while N > 2:
        N -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = tree[leaf].pop()
            tree[neighbor].remove(leaf)
            if len(tree[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    return leaves

# Two BFS passes to get the diameter.
# Time: O(n) (now two passes).
# Space: O(n).


def get_centers(N, edges):
    '''
    Gets the center(s) of a tree with N vertices 
    labeled 0,..., N - 1 and given edges.   
    >>> get_centers(2, [[0,1]])
    [0, 1]
    >>> get_centers(4, [[0,1],[0,2],[0,3]])
    [0]
    >>> get_centers(4, [[0,1],[1,2],[2,3]])
    [1, 2]
    '''
    tree = {i: set() for i in range(N)}
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)

    # BFS 1 --> Find a vertex with maximum
    #           distance from the root.
    root = 0
    q = [root]
    seen = set()
    farthest = root
    while len(q) > 0:
        new_q = []
        for v in q:
            for w in tree[v]:
                if w not in seen:
                    new_q.append(w)
            seen.add(v)

        if len(new_q) > 0:
            farthest = new_q[0]
        q = new_q

    # Node of maximum distance from root.
    # Lies on a diameter.
    v = farthest

    # BFS 2 --> Find the vertex w of maximum
    #           distance from v.  Path from
    #           v to w is a diameter.
    root = v
    q = [root]
    seen = set()

    # List that after the BFS traces out
    # a diameter.
    diameter = [root]

    # As we walk down the tree, we keep track
    # of the reverse directions.
    prev = {root: None}
    farthest = root

    while len(q) > 0:
        new_q = []
        for v in q:
            for w in tree[v]:
                if w not in seen:
                    prev[w] = v
                    new_q.append(w)
            seen.add(v)
        if len(new_q) > 0:
            farthest = new_q[0]
        q = new_q

    w = farthest

    diameter = []
    current = w
    while current is not None:
        diameter.append(current)
        current = prev[current]

    D = len(diameter)
    index = 0
    if D % 2 == 0:
        return diameter[(D-1)//2: (D-1)//2 + 2]
    return [diameter[D//2]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

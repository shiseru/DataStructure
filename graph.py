"""
    Graph ADT:
    vertices(G): return a list of all the vertices of G.
    check_adjacent(G, u, v): return whether vertices u and v are adjacentin G

    graph: G = (V, E) where V is a set of vertices and E is a set of edges.

    undirected graph - graph where edge tuples order does not matter.

    directed graph - order in edge tuples matter. (V1, V2) and (V2, V1) are different edges

    adjacent: two vertices are adjacent if there is edges between two adjacent

    path: sequence of edges between vertices U and V.

    length: the number of edges in the path.

    distance: shortest path between two vertices.

    connected graph: path exists in all of pair of vertices. Otherwise, the graph is unconnected

    degree of vertex: number of its neighbours
"""

"""
    Assume there are n vertices
    and u has m edges.
    Then running time is O(n, m) """


# O(min(m, n)) where m is a number of vertices and n is number of vertices in Graph.
def check_adjacent(G, i, j):
    u = G.vertices[i]
    v = G.vertices[j]

    for vertex in u.neighbours:
        if vertex.label == v.label:
            return True

    return False


"""
    use adjacency matrix. we can represent vertices in [n][n-1] matrix
    however, it takes O(|V|^2) space cost, for |V| -by-|V| matrix, as the edges and non-edges information have to be 
    stored in memory.
"""


def check_adjacent(G, i, j):
    return G.adjacency[i][j]


def breadth_first_search(graph, s):
    queue = []

    queue.append(s)
    s.enqueued = True

    while len(queue) != 0:
        vertex = queue.pop(0)

        for each neighbour u of v:
            if u not in queue:
                queue.append(u)

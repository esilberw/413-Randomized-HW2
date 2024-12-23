import copy
import random
import math
from itertools import combinations


class Graph:
    def __init__(self, edges_list=None):
        self.edges_list = edges_list
        self.vertices = self.compute_vertices()
        self.n = len(self.vertices)

    def set_edges_list(self, new_edges_list):
        self.edges_list = new_edges_list
        self.vertices = self.compute_vertices()
        self.n = len(self.vertices)

    def get_edges(self):
        return copy.deepcopy(self.edges_list)

    def get_vertices(self):
        return self.vertices

    def get_n(self):
        return self.n

    def compute_vertices(self):
        vertices = set()

        for edge in self.edges_list:
            # adding to the set all the vertices encountered
            vertices.add(edge[0])
            vertices.add(edge[1])

        return vertices


def contraction(graph, random_edge):
    """
        Contraction of a random edge, change the self.edges_list to adapt the graph.
        :param graph:
        :param random_edge: list of two vertices, representing an edge [u, v]
        :return: None
        """

    u, v = random_edge
    edges_list = graph.get_edges()

    # eliminate all [u, v] edges
    edges_list = [edge for edge in edges_list if edge != random_edge]

    for i in range(len(edges_list)):
        s, t = edges_list[i]
        if s == v:

            # Update the remaining edges
            edges_list[i][0] = u

        if t == v:
            edges_list[i][1] = u

    # remove self_loops
    edges_list = [edge for edge in edges_list if edge[0] != edge[1]]

    updated_edges_list = edges_list
    graph.set_edges_list(updated_edges_list)

    return graph


def contract_algo(graph, t=2):
    """
    implementation of the kurger's minimum cut algorithm.
    :return: the remaining edges_list that represented the minimum cut.
    """

    contrated_graph = copy.deepcopy(graph)

    while contrated_graph.get_n() > t:
        random_pick_e = random.choice(contrated_graph.get_edges())
        print("RANDOM_PICK:  ---", random_pick_e, "---")
        print("BEFORE CONTRACTION:\n", contrated_graph.get_edges())
        contrated_graph = contraction(contrated_graph, random_pick_e)
        print("AFTER CONTRACTION:\n", contrated_graph.get_edges())
        print("Number of vertices:", contrated_graph.get_n())

    return contrated_graph


def fast_cut_aglo(graph):
    n = graph.get_n()

    if n <= 6:
        return brute_force_min_cut(graph)

    t = math.ceil(1 + n / math.sqrt(2))

    H1 = contract_algo(copy.deepcopy(graph), t)
    H2 = contract_algo(copy.deepcopy(graph), t)

    cut_1, edges_list_1 = fast_cut_aglo(H1)
    cut_2, edges_list_2 = fast_cut_aglo(H2)

    if cut_1 < cut_2:
        return cut_1, edges_list_1
    else:
        return cut_2, edges_list_2


def brute_force_min_cut(graph):
    min_cut = float('inf')
    min_cut_edges = []
    vertices = graph.get_vertices()
    n = graph.get_n()
    edges = graph.get_edges()

    for subset_size in range(1, n):
        for subset in combinations(vertices, subset_size):  # enumerate all the possible partitions:

            partition = set(subset)

            if len(partition) == 0 or len(partition) == n or len(partition) == 1:
                continue

            cut_edges = []

            for edge in edges:
                u, v = edge
                if (u in partition and v not in partition) or (v in partition and u not in partition):
                    cut_edges.append(edge)

            # Update the minimum cut if the current cut is smaller but bigger than 0
            if 0 <= len(cut_edges) < min_cut:
                min_cut = len(cut_edges)
                min_cut_edges = cut_edges

    return min_cut, min_cut_edges


# Example graph of the picture in the lecture note and Homework II assignment:
edges_list = [
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 5],
    [3, 4], [3, 5],
    [4, 5],
    [5, 6], [3, 7], [4, 8],
    [7, 6], [7, 8], [7, 9], [7, 10],
    [8, 6], [8, 9], [8, 10],
    [9, 10], [9, 6],
    [10, 6]
]
test_contraction_list = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]
brut_force_test_edge_list = [
    [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]
]

test_brute_force_graph = Graph(brut_force_test_edge_list)
test_graph = Graph(edges_list)

fast_cut_flag = True
if fast_cut_flag:
    print(fast_cut_aglo(test_graph))
else:
    print(contract_algo(test_graph).get_edges())

#print(brute_force_min_cut(test_brute_force_graph))


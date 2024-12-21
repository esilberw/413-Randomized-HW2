import random
import math
from itertools import combinations


class Graph:
    def __init__(self, edges_list=None):
        self.edges_list = edges_list
        self.n, self.vertices = self.compute_num_vertices()

    def get_edges(self):
        return self.edges_list

    def get_vertices(self):
        return self.vertices

    def compute_num_vertices(self):
        vertices = set()

        for edge in self.edges_list:
            # adding to the set all the vertices encountered
            vertices.add(edge[0])
            vertices.add(edge[1])

        self.n = len(vertices)
        return self.n, vertices

    def contraction(self, random_edge):
        """
        Contraction of a random edge, change the self.edges_list to adapt the graph.
        :param random_edge: list of two vertices, representing an edge [u, v]
        :return: None
        """

        u, v = random_edge

        while random_edge in self.edges_list:
            # eliminate all edges connecting u and v (because multi-graph --> need while loop)
            self.edges_list.remove(random_edge)

        for i in range(len(self.edges_list)):
            s, t = self.edges_list[i]
            if s == v:
                # Update the remaining edges
                if t != u:  # avoid self loops
                    self.edges_list[i][0] = u
            if t == v:
                if s != u:
                    self.edges_list[i][1] = u

        self.compute_num_vertices()

    def contract_algo(self, t=2):
        """
        implementation of the kurger's minimum cut algorithm.
        :return: the remaining edges_list that represented the minimum cut.
        """
        while self.n > t:
            random_pick_e = random.choice(self.edges_list)
            print("RANDOM_PICK:  ---", random_pick_e, "---\n", self.edges_list)
            self.contraction(random_pick_e)
            print("AFTER CONTRACTION:\n", self.edges_list)
            print("Number of vertices:", self.n)

        return self.edges_list

    def fast_cut_aglo(self):
        self.compute_num_vertices()  # update n because edges_list change
        if self.n <= 6:
            return self.brute_force_min_cut()

        else:
            t = math.ceil(1 + self.n / math.sqrt(2))
            H1 = self.contract_algo(t)
            H2 = self.contract_algo(t)

            self.edges_list = H1
            cut_1 = self.fast_cut_aglo()

            self.edges_list = H2
            cut_2 = self.fast_cut_aglo()

            return min(cut_1, cut_2)

    def brute_force_min_cut(self):
        min_cut = float('inf')
        min_cut_edges = []
        for subset_size in range(1, self.n // 2 + 1):
            for subset in combinations(self.get_vertices(), subset_size):
                partition = set(subset)

                if len(partition) == 0 or len(partition) == self.n:
                    continue  # Ignorer les partitions triviales

                cut_edges = []
                for edge in self.edges_list:
                    u, v = edge
                    if (u in partition and v not in partition) or (v in partition and u not in partition):
                        cut_edges.append(edge)

                # Update the minimum cut if the current cut is smaller
                if len(cut_edges) < min_cut:
                    min_cut = len(cut_edges)
                    min_cut_edges = cut_edges

        return min_cut


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

brut_force_test_edge_list = [
    [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]
]

fast_cut_aglo = True

# test_graph = Graph(brut_force_test_edge_list)
# print(test_graph.brute_force_min_cut())


test_graph = Graph(edges_list)
if fast_cut_aglo:
    print(test_graph.fast_cut_aglo())
else:
    test_graph.contract_algo()

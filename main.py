import random


class Graph:
    def __init__(self, vertices, edges_list=None):
        self.n = vertices
        self.edges_list = edges_list

    def get_edges(self):
        return self.edges_list

    def get_vertices(self):
        return self.n

    def contraction(self, random_edge):
        """
        Contraction of a random edge, change the self.edges_list to adapt the graph.
        :param random_edge: list of two vertices, representing an edge [u, v]
        :return: None
        """
        self.n -= 1  # decrease the number of vertices # ro
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

    def contract_algo(self):
        """
        implementation of the kurger's minimum cut algorithm.
        :return: the remaining edges_list that represented the minimum cut.
        """
        while self.n >= 2:
            random_pick_e = random.choice(self.edges_list)
            print("RANDOM_PICK:  ---", random_pick_e, "---\n", self.edges_list)
            self.contraction(random_pick_e)
            print("AFTER CONTRACTION:\n", self.edges_list)
            print("Nombre de sommets:", self.n)

        return self.edges_list

    def fast_cut_aglo(self):
        return None


"""    def generate_particular_graph(self, graph_type, num_edges):
        edges_list = []
        match graph_type:
            case "complete":
                edges_list = [(u, v) for u in range(self.n) for v in range(u + 1, self.n)]

            case "star":
                edge_list = [(0, i) for i in range(self.n) if i != 0]

            case "grid":
                edges_list = []

            case "random":
                # random multigraph
                edges_list = []

            case "multigraph":
                # deterministic multigraph
                edges_list = []

        return edges_list

"""

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
test_graph = Graph(10, edges_list)
test_graph.contract_algo()
print(test_graph.get_edges())

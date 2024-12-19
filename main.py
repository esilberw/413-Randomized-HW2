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
        Contraction of an edge, change the self.edges_list to adapt the graph.
        :param random_edge: list of two vertices, representing an edge [u, v]
        :return: None
        """
        self.n -= 1
        u, v = random_edge

        while random_edge in self.edges_list:
            # eliminates all edges connecting u and v
            self.edges_list.remove(random_edge)

        for i in range(len(self.edges_list)):
            s, t = self.edges_list[i]
            if s == v:
                self.edges_list[i][0] = u
            if t == v:
                self.edges_list[i][1] = u


    def contract_algo(self):
        for i in range(1, self.n - 1):
            random_pick_e = random.choice(self.edges_list)
            self.contraction(random_pick_e)

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



edges_list = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]
testGraph = Graph(4, edges_list)
testGraph.contraction([2, 3])
print(testGraph.get_edges())

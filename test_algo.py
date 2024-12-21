class test_algo:
    def __init__(self):
        return None

def generate_particular_graph(self, graph_type, num_edges):
    edges_list = []
    if graph_type == "complete":
        edges_list = [(u, v) for u in range(self.n) for v in range(u + 1, self.n)]

    elif graph_type == "star":
        edge_list = [(0, i) for i in range(self.n) if i != 0]

    elif graph_type == "grid":
        edges_list = []

    elif graph_type == "random":
        # random multigraph
        edges_list = []

    elif graph_type == "multigraph":
        # deterministic multigraph
        edges_list = []

    return edges_list

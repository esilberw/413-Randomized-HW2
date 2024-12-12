import random

class Graph:

    def __init__(self, vertices, edges_list):
        self.n = vertices
        self.edges_list = edges_list

    def get_edges(self):
        return self.edges_list

    def get_vertices(self):
        return self.n

    def remove_vertex(self, vertex_to_remove):
        self.n -= 1
        for vertex_to_remove in self.edges_list:



    def generate_random_graph(self):
        graph_g = []
        return graph_g



def contract_algo(graph_g):
    for i in range(graph_g.vertex):
        random_pick_e = random.choice(graph_g.edge)
        graph_g.remove(random_pick_e)




def fast_cut_aglo(graph_g):
    return None





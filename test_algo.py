import copy

from matplotlib import pyplot as plt
import main
import time
import random


def generate_particular_graph(n, graph_type):
    edges_list = []
    min_cut_size = 0
    if graph_type == "complete":
        edges_list = [[u, v] for u in range(n) for v in range(u + 1, n)]
        min_cut_size = n - 1

    elif graph_type == "bipartite_complete":
        if n % 2 == 0:
            m = n // 2
            set1 = list(range(m))
            set2 = list(range(m, n))

            edges_list = [[u, v] for u in set1 for v in set2]
            min_cut_size = m
        else:
            raise ValueError("For this type of graph, the number of vertices must be EVEN")

    elif graph_type == "random":
        edges_list = []
        for _ in range(n * 2):
            u, v = random.randint(0, n - 1), random.randint(0, n - 1)
            if u != v:  # avoid self_loops
                edges_list.append([u, v])
                edges_list.append([u, v])  # ensure that there is at least two edges

        # adding one new vertex i = n + 1 and connect it to a random vertex of the graph:
        new_vertex = n + 1
        edges_list.append([random.randint(0, n - 1), new_vertex])
        min_cut_size = 1  # because this new edge is the min_cut

    return main.Graph(edges_list), min_cut_size


def test_contract_algo(graph):
    res_graph = main.contract_algo(graph).get_edges()
    return len(res_graph)


def test_fast_cut_algo(graph, expected_result):
    res_fast_cut = main.fast_cut_aglo(graph)
    assert res_fast_cut[0] == expected_result
    return res_fast_cut[0]


def test_contract_algo_multiruns(graph, expected_result, runs=100, budget_time=1.0):
    result_tab = []
    succeed_res = 0

    for _ in range(runs):
        cut_size = test_contract_algo(graph)
        if cut_size == expected_result:
            succeed_res += 1

        result_tab.append(cut_size)

    succeed_proba = succeed_res / runs

    return result_tab, succeed_proba


def test_fast_cut_algo_multiruns(graph, expected_result, runs=100, budget_time=1.0):
    result_tab = []
    succeed_res = 0
    for _ in range(runs):

        cut_size = test_contract_algo(graph)
        if cut_size == expected_result:
            succeed_res += 1

        result_tab.append(cut_size)

    succeed_proba = succeed_res / runs

    return result_tab, succeed_proba


def plot_result_contract_algo(result_tab, expected_result):
    plt.plot(result_tab, label="Result of the tests", color='blue')
    plt.axhline(y=expected_result, color='g', linestyle='--', label=f'Expected result = {expected_result:.3f}')
    plt.xlabel("Test number")
    plt.ylabel("Results of the tests")
    plt.title("Contract algorithm")
    plt.show()


def plot_succeed_ratio_contract_algo(succeed_proba):
    plt.axhline(y=succeed_proba, color='g', linestyle='--', label=f'Expected result = {succeed_proba:.3f}')
    plt.xlabel("Test number")
    plt.ylabel("Succeed Probability Rate")
    plt.title("Contract algorithm")
    plt.show()


def plot_result_fast_cut_algo(result_tab, expected_result):
    plt.plot(result_tab, label="Result of the tests", color='blue')
    plt.axhline(y=expected_result, color='g', linestyle='--', label=f'Expected result = {expected_result:.3f}')
    plt.xlabel("Test number")
    plt.ylabel("Results of the tests")
    plt.title("Fast Cut algorithm")
    plt.show()


def plot_succeed_ratio_fast_cut_algo(succeed_proba):
    plt.axhline(y=succeed_proba, color='g', linestyle='--', label=f'Expected result = {succeed_proba:.3f}')
    plt.xlabel("Test number")
    plt.ylabel("Succeed Probability Rate")
    plt.title("Fast Cut algorithm")
    plt.show()


graph_random, lowest_min_cut = generate_particular_graph(100, "random")

# test OK without time, need with time constraint:
graph_complete, min_cut_complete = generate_particular_graph(100, "complete")

# test OK without time, need with time constraint:
graph_bipartite_complete, min_cut_bipartite_complete = generate_particular_graph(100, "bipartite_complete")

print(lowest_min_cut)
print(graph_random.get_edges())

graph_random_copy = copy.deepcopy(graph_random)

test = test_contract_algo_multiruns(graph_random, lowest_min_cut, 100, 1.0)
print(test)
plot_result_contract_algo(test[0], lowest_min_cut)
plot_succeed_ratio_contract_algo(test[1])


# to be sure that we test the both algorithms on the same random graph.
test_2 = test_fast_cut_algo_multiruns(graph_random_copy, lowest_min_cut, 100, 1.0)
print(test_2)
plot_result_fast_cut_algo(test[0], lowest_min_cut)
plot_succeed_ratio_fast_cut_algo(test[1])

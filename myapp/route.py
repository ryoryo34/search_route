import networkx as nx
from itertools import permutations
from graph import make_graph1, make_graph2

def search_dijkstra(start, goal):
    G = make_graph1()
    return nx.dijkstra_path(G, start, goal)

def search_sales(spots):
    # 指定した観光地で別のサブグラフを作成
    G = make_graph2()
    subgraph = G.subgraph(spots)
    shortest_path = None
    shortest_distance = float('inf')

    # 指定した観光地を通る経路の全ての組み合わせを作成する
    node_permutations = permutations(spots)

    # 全ての組み合わせを試し、最短経路を見つける
    for perm in node_permutations:
        total_distance = 0
        for i in range(len(perm) - 1):
            total_distance += nx.shortest_path_length(subgraph, source=perm[i], target=perm[i + 1], weight='weight')

        if total_distance < shortest_distance:
            shortest_path = perm
            shortest_distance = total_distance

    return shortest_path, shortest_distance
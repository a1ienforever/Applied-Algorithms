import concurrent.futures
import csv
import threading
from concurrent.futures import ThreadPoolExecutor

from lb1.RandomGraph import Graph, OrientedGraph, Cluster
from lb2.BFS_DFS import dfs, bfs
from tqdm import tqdm


def read_edges_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # skip header row
        edges = [(int(row[0]), int(row[1])) for row in tqdm(reader)]
        return edges


def edges_to_adjacency_list(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph


# TODO создать два прохода в ширину и в глубину
# Записать в csv
def main():
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\graph.csv'
    edges = read_edges_from_csv(path)
    graph = edges_to_adjacency_list(edges)

    with ThreadPoolExecutor() as executor:
        result = [
            executor.submit(bfs, graph, 1),
            executor.submit(dfs, graph, 1)
        ]

        concurrent.futures.wait(result)

    print(*result)


if __name__ == '__main__':
    main()

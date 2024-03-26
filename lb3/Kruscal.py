import csv
import time

from collections import defaultdict
from tqdm import tqdm


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph.keys())
    included_vertices = set()
    edges = ((vertex, neighbor, weight) for vertex, neighbors in graph.items() for neighbor, weight in neighbors)

    edges = sorted(edges, key=lambda x: x[2])
    pbar = tqdm(total=100000, desc='kruscal')

    for edge in edges:
        pbar.update(1)
        vertex1, vertex2, weight = edge
        if vertex1 not in included_vertices or vertex2 not in included_vertices: # remark
            if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
                disjoint_set.union(vertex1, vertex2)
                minimum_spanning_tree.append(edge)
                included_vertices.update([vertex1, vertex2])
    pbar.close()
    return minimum_spanning_tree


def read_graph_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pbar = tqdm(total=len(lines), desc='reading')
    graph1 = {}
    with open(file_path, 'r') as file:
        for line in file:
            pbar.update(1)
            if line[0] != 'V':
                parts = line.strip().split(';')
                vertex_id = int(parts[0])
                edges = parts[1:]
                edges_info = []
                for edge in edges:
                    # Разбиваем информацию о ребре по символу "!"
                    neighbor, weight = map(int, edge.split('!'))
                    edges_info.append((neighbor, weight))
                graph1[vertex_id] = edges_info
    graph = {}
    for i in range(len(graph1)):
        graph[i] = graph1.get(i)
    pbar.close()
    return graph


def sorting_by_weight(graph):
    pbar = tqdm(total=len(graph), desc='sorted graph')
    for vertex in graph:
        pbar.update(1)
        graph[vertex].sort(key=lambda x: x[1])
    pbar.close()
    return graph


def write_to_csv(file_path, graph):
    pbar = tqdm(total=len(graph), desc='writing')
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["vertex", "neighbors"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')

        writer.writeheader()
        for row, neighbours in graph.items():
            pbar.update(1)
            writer.writerow(
                {"vertex": str(row) + ',', "neighbors": ",".join(str(x[0]) + ";" + str(x[1]) for x in neighbours)})
    pbar.close()


if __name__ == '__main__':

    # Путь к файлу graph.csv
    file_path = "graph.csv"

    # Считываем данные и строим граф в виде словаря
    graph = read_graph_file(file_path)
    graph = sorting_by_weight(graph)
    minimum_spanning_tree = kruskal(graph)

    adjacency_lists = {vertex: [] for vertex in graph.keys()}
    for edge in minimum_spanning_tree:
        vertex1, vertex2, weight = edge
        adjacency_lists[vertex1].append((vertex2, weight))
        adjacency_lists[vertex2].append((vertex1, weight))
    # for vertex, neighbors in adjacency_lists.items():
    #     print(f"Vertex {vertex}: {neighbors}")

    write_to_csv('ostov.csv', adjacency_lists)

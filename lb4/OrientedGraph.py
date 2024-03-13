import csv
import random

import networkx as nx
from matplotlib import pyplot as plt
from tqdm import tqdm

from GraphReader import GraphReader


class Node:
    def __init__(self, data=None):
        self.neighbors = set()
        self.data = data


class OrientedGraph:
    def __init__(self):
        self.list_node = list()

    def create_graph(self, num_vertices, avg_connectivity):
        u = int(avg_connectivity - (avg_connectivity / 2))
        v = int(avg_connectivity + (avg_connectivity / 2))

        for i in range(1, num_vertices + 1):
            self.list_node.append(Node(i))
        pbar = tqdm(total=len(self.list_node), desc='creating graph')

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            pbar.update(1)

            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node not in node1.neighbors and node1 not in node.neighbors and node1 != node and len(
                        node.neighbors) < v and len(node1.neighbors) < v:
                    node.neighbors.add(node1)

        pbar.close()
        return self

    def write_graph_to_csv2(self, filename, graph):
        with open(filename, 'w', newline='') as csvfile:
            pbar = tqdm(total=len(self.list_node), desc='writing graph')

            writer = csv.writer(csvfile, delimiter=' ')
            for node in graph.list_node:
                pbar.update(1)
                writer.writerow([f'{node.data},', ','.join(str(n.data) for n in node.neighbors)])
            pbar.close()
def main():
    graph = OrientedGraph().create_graph(10, 4)
    graph.write_graph_to_csv2('oriented_graph.csv', graph)
    gr = GraphReader()
    path = "C:\\Users\\artyo\\PycharmProjects\Applied Algorithms\\lb4\\oriented_graph.csv"
    graph = gr.read_graph_from_csv(path)
    for key, value in graph.items():
        print(key, ":", value)

    G = nx.DiGraph()

    # Добавление ребер в граф на основе словаря смежности
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Рассчитываем позиции вершин в графе
    pos = nx.spring_layout(G)

    # Отрисовка графа
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold",
            arrows=True)

    # Показать граф
    plt.show()


if __name__ == '__main__':
    main()
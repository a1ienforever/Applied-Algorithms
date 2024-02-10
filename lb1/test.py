import csv
import random
from collections import defaultdict


class Node:
    def __init__(self, data=None):
        self.nodes = set()
        self.data = data

    def __str__(self):
        nodes = self.print_nodes()
        return f"{self.data}: {nodes}"

    def print_nodes(self):
        nodes = ''
        for node in self.nodes:
            nodes += str(node.data) + ','
        return nodes


class Graph:
    def __init__(self):
        self.list_node = []
        self.sum_conn = 0

    def create_connected_graph(self, num_vertices, avg_connectivity):
        u = int(avg_connectivity - (avg_connectivity / 2))
        v = int(avg_connectivity + (avg_connectivity / 2))
        # visited = set()
        for i in range(1, num_vertices + 1):
            self.list_node.append(Node(i))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            self.sum_conn += rand_conn_num
            # nodes = set(self.list_node) - visited
            for _ in range(rand_conn_num):
                # node1 = random.choice(tuple(nodes))
                node1 = random.choice(self.list_node)
                if node1 not in node.nodes and node1 != node:
                    node.nodes.add(node1)
                    node1.nodes.add(node)
                    # visited.add(node1)

        return self

    def write_graph_to_csv(self, filename, graph):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            # Write vertices
            writer.writerow(['Vertices'])
            writer.writerow([node.data for node in graph.list_node])

            # Write adjacency list
            writer.writerow(['Adjacency List'])
            for node in graph.list_node:
                writer.writerow([' '.join(str(n.data) for n in node.nodes)])





    # def average_connectivity(self):
    #     adjacency_matrix = defaultdict(int)
    #
    #     for node in self.list_node:
    #         for connected_node in node.nodes:
    #             adjacency_matrix[(node.data, connected_node.data)] = 1
    #             adjacency_matrix[(connected_node.data, node.data)] = 1
    #
    #     total_edges = sum(adjacency_matrix.values())
    #     num_vertices = len(self.list_node)
    #     avg = total_edges / num_vertices
    #     return avg


def main():
    graph = Graph()
    graph1 = graph.create_connected_graph(10, 5)
    # print(graph1.average_connectivity())
    # print(graph1.is_connected())
    graph.write_graph_to_csv('graph.csv', graph1)
    for node in graph1.list_node:
        print(node.__str__())


if __name__ == "__main__":
    main()

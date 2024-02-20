import csv
import random
from random import randint


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


class Cluster:
    def __init__(self):
        self.nodes = set()

    def size_graphs(self, num_vertices):
        graphs = []
        num = 0
        groups = {}
        new_arr = []
        while num_vertices > num:
            if num_vertices > 10:
                count_vert = randint(0, int(num_vertices / 10))
            else:
                count_vert = randint(0, int(num_vertices))
            num_vertices -= count_vert
            graphs.append(count_vert)

        for num in graphs:
            if num in groups:
                groups[num] += num
            else:
                groups[num] = num

        for num, total in groups.items():
            new_arr.append(total)
        return new_arr

    def create_disconnected_graph(self, num_vertices, avg_connectivity):
        size_graphs = self.size_graphs(num_vertices)

        for i in range(len(size_graphs)):
            self.nodes.add(Graph().create_connected_graph(size_graphs[i], avg_connectivity))
        return self

    def print(self):
        for graph in self.nodes:
            for node in graph.list_node:
                print(node.__str__())
            print('-----------------------')
        print(len(self.nodes))


class OrientedGraph:
    def __init__(self):
        self.list_node = list()
        self.sum_conn = 0

    def create_connected_graph(self, num_vertices, avg_connectivity):
        u = int(avg_connectivity - (avg_connectivity / 2))
        v = int(avg_connectivity + (avg_connectivity / 2))

        for i in range(1, num_vertices + 1):
            self.list_node.append(Node(i))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            self.sum_conn += rand_conn_num
            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node1 != node:
                    node.nodes.add(node1)
        # print(2 * edge / num_vertices)
        return self

    def print(self):
        for node in self.list_node:
            print(node.__str__())


class Graph:
    def __init__(self):
        self.list_node = list()
        self.sum_conn = 0

    def create_connected_graph(self, num_vertices=None, avg_connectivity=None):
        u = int(avg_connectivity - (avg_connectivity / 2))
        v = int(avg_connectivity + (avg_connectivity / 2))
        edge = 0
        for i in range(1, num_vertices + 1):
            self.list_node.append(Node(i))

        print(len(self.list_node))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node not in node1.nodes and node1 not in node.nodes and node1 != node and len(
                        node.nodes) < v and len(node1.nodes) < v:
                    node.nodes.add(node1)
                    node1.nodes.add(node)
        # print(2 * edge / num_vertices)
        return self

    # def write_graph_to_csv(self, filename, graph):
    #     with open(filename, 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile, delimiter=' ')
    #         for node in graph.list_node:
    #             writer.writerow([f'{node.data} ', ' '.join(str(n.data) for n in node.nodes)])

    # def write_graph_to_csv(self, filename, graph):
    #     with open(filename, 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile, delimiter=' ')
    #
    #         # Write vertices
    #         writer.writerow(f'Vertices;Abjacency_List')
    #         for node in graph.list_node:
    #             writer.writerow([f'{node.data}', ' '.join(str(n.data) for n in node.nodes)])
    #             print([f'{node.data},', ','.join(str(n.data) for n in node.nodes)])

    def write_graph_to_csv(self, file_name, graph):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for vertex in graph.list_node:
                for neighbor in vertex.nodes:
                    writer.writerow([vertex.data, neighbor.data])

    def print(self):
        for node in self.list_node:
            print(node.__str__())


def main():
    with open("C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\Configuration", mode='r') as config:
        config_reader = config.read()
        arr_param = config_reader.split(' ')
        num_vertices = int(arr_param[0])
        is_connected = arr_param[1] == 'y'
        avg_connectivity = int(arr_param[2])

        # Generate the graph

        if is_connected:
            graph = Graph().create_connected_graph(num_vertices, avg_connectivity)
            graph.print()
        else:
            graph = Cluster().create_disconnected_graph(num_vertices, avg_connectivity)
            graph.print()

    graph.write_graph_to_csv('graph.csv', graph)

    # graph = Graph().create_connected_graph(10000, 10)
    # graph.print()


if __name__ == "__main__":
    main()

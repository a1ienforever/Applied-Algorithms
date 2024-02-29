import csv
import random
from random import randint


class Node:
    def __init__(self, data=None, weight=None):
        self.neighbors = {}
        self.data = data

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight
        neighbor.neighbors[self] = weight


    def __str__(self):
        nodes = self.print_nodes()
        return f"{self.data}; {nodes}"

    def print_nodes(self):
        nodes = ''
        for node in self.neighbors:
            nodes += str(node.data) + ':' + str(node.data) + ','
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
            self.list_node.append(Node(i, ))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            self.sum_conn += rand_conn_num
            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node1 != node:
                    node.neighbors.add(node1)
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
        for i in range(1, num_vertices + 1):
            self.list_node.append(Node(i))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node not in node1.neighbors and node1 not in node.neighbors and node1 != node and len(
                        node.neighbors) < v and len(node1.neighbors) < v:
                    # weight = round(random.randint(1, 10), 1)
                    node.add_neighbor(node1)
                    node1.add_neighbor(node)

            if len(node.neighbors) == 0:
                node.add_neighbor(node1,)
                node1.add_neighbor(node,)
        return self

    def write_graph_to_csv(self, file_name, graph, type=None):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for vertex in graph.list_node:
                for neighbor in vertex.neighbors:
                    if type == 'weighted':
                        weight = random.randint(1, 10)
                    writer.writerow([vertex.data, neighbor.data, weight])

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

        if is_connected:
            graph = Graph().create_connected_graph(num_vertices, avg_connectivity)
            graph.print()
        else:
            graph = Cluster().create_disconnected_graph(num_vertices, avg_connectivity)
            graph.print()

    graph.write_graph_to_csv('graph.csv', graph, 'weighted')


if __name__ == "__main__":
    main()

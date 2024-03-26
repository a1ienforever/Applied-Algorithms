import csv
import random

from tqdm import tqdm

from GraphReader import GraphReader


class Node:
    def __init__(self, data=None):
        self.neighbors = set()
        self.data = data

    def __str__(self):
        nodes = self.print_nodes()
        return f"{self.data}; {nodes}"

    def print_nodes(self):
        nodes = ''
        for node in self.neighbors:
            nodes += str(node.data) + ':' + str(node.data) + ','
        return nodes

class Graph:
    def __init__(self):
        self.list_node = list()

    def create_graph(self, num_vertices=None, avg_connectivity=None):
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

            if len(node.neighbors) == 0:
                node.neighbors.add(node1, )

        pbar.close()
        return self

    def print(self):
        for node in self.list_node:
            print(node.__str__())

    def write_graph_to_csv2(self, filename, graph):
        with open(filename, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile, delimiter=' ')
            for node in graph.list_node:
                writer.writerow([f'{node.data},', ','.join(str(n.data) for n in node.neighbors)])


def main():

    graph = Graph()

    with open("C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb4\\config.txt", mode='r') as config:
        config_reader = config.read()
        arr_param = config_reader.split(' ')
        num_vertices = int(arr_param[0])
        is_connected = arr_param[1] == 'y'
        avg_connectivity = int(arr_param[2])

        graph.create_graph(num_vertices, avg_connectivity)
        graph.write_graph_to_csv2('oriented_graph.csv', graph)

if __name__ == '__main__':
    main()
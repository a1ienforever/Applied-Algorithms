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
            nodes += str(node.data) + ' '
        return nodes


class Cluster:
    def __init__(self):
        self.nodes = set()

    def size_graphs(self, num_vertices):
        nums = []
        num = 0
        groups = {}
        new_arr = []
        while num_vertices > num:
            if num_vertices > 10:
                count_vert = randint(0, int(num_vertices / 10))
            else:
                count_vert = randint(0, int(num_vertices))
            num_vertices -= count_vert
            nums.append(count_vert)

        for num in nums:
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

class Graph:
    def __init__(self):
        self.list_node = list()
        self.sum_conn = 0

    def create_connected_graph(self, num_vertices=None, avg_connectivity=None, num_start=1):
        u = int(avg_connectivity - (avg_connectivity / 2))
        v = int(avg_connectivity + (avg_connectivity / 2))
        for i in range(num_start, num_vertices + 1):
            self.list_node.append(Node(i))

        for node in self.list_node:
            rand_conn_num = random.randint(u, v)
            self.sum_conn += rand_conn_num
            for _ in range(rand_conn_num):
                node1 = random.choice(self.list_node)
                if node1 not in node.nodes and node1 != node:
                    node.nodes.add(node1)
                    node1.nodes.add(node)

        return self

    def write_graph_to_csv(self, filename, graph):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')

            # Write vertices
            writer.writerow(f'Vertices;Abjacency_List')
            for node in graph.list_node:
                writer.writerow([f'{node.data};', ';'.join(str(n.data) for n in node.nodes)])
                print([f'{node.data};', ';'.join(str(n.data) for n in node.nodes)])

    def print(self):
        for node in self.list_node:
            print(node.__str__())



def main():
    graph_conn = Graph().create_connected_graph(50, 5)
    graph_conn.print()
    graph_conn.write_graph_to_csv('graph.csv', graph_conn)


    # graph_disconn = Cluster().create_disconnected_graph(50, 5)
    # graph_disconn.print()

if __name__ == "__main__":
    main()

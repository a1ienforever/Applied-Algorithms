import random


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


class Graph:
    def __init__(self):
        self.list_node = []
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
                if node1 not in node.nodes and node1 != node:
                    node.nodes.add(node1)
                    node1.nodes.add(node)
        return self

    def print_avg_conn(self):
        avg = 2 * self.sum_conn / len(graph.list_node)
        return avg


graph = Graph()
graph1 = graph.create_connected_graph(100000, 5)
for node in graph1.list_node:
    print(node.__str__())

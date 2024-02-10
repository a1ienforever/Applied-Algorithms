import networkx as nx
import random
import csv
import matplotlib.pyplot as plt
import scipy as sc


# Generate random graph
def generate_random_connected_graph(num_vertices, avg_connectivity):
    G = nx.Graph()
    G.add_nodes_from(range(1, num_vertices + 1))
    num_edges = int(avg_connectivity * num_vertices / 2)

    while len(G.edges()) < num_edges:
        node1 = random.randint(1, num_vertices)
        node2 = random.randint(1, num_vertices)
        while node1 == node2 or (node1, node2) in G.edges() or (node2, node1) in G.edges():
            node1 = random.randint(1, num_vertices)
            node2 = random.randint(1, num_vertices)
        G.add_edge(node1, node2)
    return G


def generated_random_disconnected(num_vertices):
    graph = nx.Graph()

    # Генерация рандомного количества несвязных компонент
    num_components = random.randint(1, 5)

    # Генерация несвязных компонент
    for i in range(num_components):
        # Выбор рандомного количества вершин
        vertices = list(range(num_vertices))
        # Создание полного графа
        component_graph = nx.complete_graph(vertices)
        # Удаление рандомного количества ребер
        num_edges_to_remove = random.randint(1, len(component_graph.edges))
        edges_to_remove = random.sample(component_graph.edges, num_edges_to_remove)
        for edge in edges_to_remove:
            component_graph.remove_edge(*edge)
        # Добавление графа в основной граф
        graph = nx.disjoint_union(graph, component_graph)

    return graph


# Save the graph in CSV format
def save_graph_to_csv(G, filename):
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["source", "target"])
        for edge in G.edges():
            csv_writer.writerow(list(edge))


def average_degree(G):
    return 2 * G.number_of_edges() / G.number_of_nodes()


# Show the graph in PNG format
def show_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()


def main():
    # Get input parameters
    with open("C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\Configuration", mode='r') as config:
        config_reader = config.read()
        arr_param = config_reader.split(' ')
        num_vertices = int(arr_param[0])
        is_connected = arr_param[1] == 'y'
        avg_connectivity = int(arr_param[2])

        # Generate the graph

        if is_connected:
            G = generate_random_connected_graph(num_vertices, avg_connectivity)
            show_graph(G)
        else:
            #  G = generated_random_disconnected(num_vertices, int((avg_connectivity - 1) * num_vertices / 2))
            G = generated_random_disconnected(num_vertices)
            show_graph(G)

        save_graph_to_csv(G, "random_graph.csv")
        print(average_degree(G))
        # Save the graph to CSV


if __name__ == '__main__':
    main()

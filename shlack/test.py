import random
from tqdm import tqdm


def generate_acyclic_graph(num_vertices, avg_degree):
    graph = [[] for _ in range(num_vertices)]

    for i in tqdm(range(num_vertices)):
        for j in range(i + 1, num_vertices):
            if random.random() < avg_degree / (num_vertices - i - 1):
                graph[i].append(j)

    return graph


def save_graph_to_csv(graph, filename):
    with open(filename, 'w') as file:
        for i, neighbors in enumerate(graph):
            file.write(f'{i},{",".join(map(str, neighbors))}\n')


# Пример использования
num_vertices = 100000
avg_degree = 10
filename = 'acyclic_graph.csv'

graph = generate_acyclic_graph(num_vertices, avg_degree)
save_graph_to_csv(graph, filename)

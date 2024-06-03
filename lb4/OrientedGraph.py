import csv
import random
from tqdm import tqdm


def generate_random_directed_graph(num_vertices, avg_connectivity):
    # Инициализируем граф как словарь множеств
    graph = {vertex: set() for vertex in range(1, num_vertices + 1)}

    # Вычисляем ожидаемое количество рёбер
    expected_edges = int(num_vertices * avg_connectivity)

    # Создаем прогресс-бар для отслеживания хода выполнения
    with tqdm(total=expected_edges, desc="Генерация графа") as pbar:
        # Создаем рёбра в графе
        while expected_edges > 0:
            # Выбираем случайную пару вершин
            src_vertex = random.randint(1, num_vertices)
            dest_vertex = random.randint(1, num_vertices)

            # Проверяем, что ребро не существует и что это не петля
            if dest_vertex != src_vertex and dest_vertex not in graph[src_vertex]:
                # Добавляем ребро
                graph[src_vertex].add(dest_vertex)
                expected_edges -= 1
                pbar.update(1)  # Обновляем прогресс-бар

    return graph

def write_graph_to_csv2(filename, graph):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for node in graph.keys():
            writer.writerow([f'{node},', ','.join(str(n) for n in graph[node])])



# Пример использования
num_vertices = 100000
avg_connectivity = 1  # Средняя связность (от 0 до 1)

random_directed_graph = generate_random_directed_graph(num_vertices, avg_connectivity)
write_graph_to_csv2('oriented_graph.csv', random_directed_graph)
print(random_directed_graph)

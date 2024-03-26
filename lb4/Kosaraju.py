import csv
import sys
from tqdm import tqdm
from GraphReader import GraphReader



def kosaraju(graph):
    total_iterations = len(graph)  # Подсчитываем общее количество итераций
    progress_bar = tqdm(total=total_iterations, desc="Kosaraju Algorithm")

    def dfs(node, visited, stack):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)
          # Обновляем прогрессбар после каждого вызова dfs

    def transpose(graph):
        transposed = {node: [] for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                transposed[neighbor].append(node)
        return transposed

    def dfs_second(node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in transposed_graph[node]:
            if not visited[neighbor]:
                dfs_second(neighbor, visited, component)
        progress_bar.update(1)  # Обновляем прогрессбар после каждого вызова dfs_second

    visited = {node: False for node in graph.keys()}
    stack = []
    for node in graph:
        if not visited[node]:
            dfs(node, visited, stack)

    transposed_graph = transpose(graph)
    visited = {node: False for node in graph}
    strong_components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_second(node, visited, component)
            strong_components.append(component)

    progress_bar.close()  # Закрываем прогрессбар после завершения алгоритма
    return strong_components


# Пример использования:
def main():
    gr = GraphReader()
    path = "C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb4\\oriented_graph.csv"
    graph = gr.read_graph_from_csv(path)
    print(graph)
    ccs_list = kosaraju(graph[0])
    ccs = max(ccs_list, key=len)
    print(ccs)

    with open('cliques.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(ccs)


if __name__ == '__main__':
    main()

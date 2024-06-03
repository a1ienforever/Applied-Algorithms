import csv
import sys

sys.setrecursionlimit(10000)

def kosaraju(graph):
    def dfs(node, visited, stack):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

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

    # Создаем смежные списки для максимальной компоненты
    max_component = max(strong_components, key=len)
    subgraph = {node: set(graph[node] & set(max_component)) for node in max_component}
    return subgraph


def read_graph_from_csv(filename):
    graph = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            node = int(row[0][:-1])
            neighbors = [int(n) for n in row[1].split(',') if n.strip()]
            graph[node] = set(neighbors)
    return graph


def main():
    path = "oriented_graph.csv"
    graph = read_graph_from_csv(path)
    max_subgraph = kosaraju(graph)
    print(max_subgraph)

    with open('max_subgraph.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for node, neighbors in max_subgraph.items():
            writer.writerow([node] + list(neighbors))


if __name__ == '__main__':
    main()

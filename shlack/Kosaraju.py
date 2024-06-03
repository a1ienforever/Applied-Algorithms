from GraphReader import GraphReader


def transpose_graph(graph):
    num_vertices = len(graph)
    transposed_graph = [[] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in graph[i]:
            transposed_graph[j].append(i)
    return transposed_graph


def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)


def dfs_reverse(graph, vertex, visited, component):
    visited[vertex] = True
    component.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_reverse(graph, neighbor, visited, component)


def kosaraju(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    stack = []
    for i in range(num_vertices):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    transposed_graph = transpose_graph(graph)
    visited = [False] * num_vertices
    components = []
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs_reverse(transposed_graph, vertex, visited, component)
            components.append(component)

    return components

if __name__ == '__main__':
    gr = GraphReader()
    path = "C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\shlack\\acyclic_graph.csv"
    graph = gr.read_graph_from_csv(path)
    ccs = kosaraju(graph)
    print(ccs)
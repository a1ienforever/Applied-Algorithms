import csv

from lb1.RandomGraph import Graph, Cluster, OrientedGraph


# def dfs(graph):
#     i = 0
#     visited = set()
#     for node in graph:
#         if node not in visited:
#             stack = [node]
#             while stack:
#                 current = stack.pop()
#                 if current not in visited:
#                     visited.add(current)
#                     stack.extend(current - visited)
#         i += 1
#         print(i)
#     return visited

def dfs(graph, start_vertex):
    visited = set()
    stack = [start_vertex]

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.add(current_vertex)
            print(current_vertex)
            stack.extend(graph[current_vertex] - visited)



def bfs(graph, start):
    i = 0
    visited = set()
    queue = [start]
    for node in graph.list_node:
        if node not in visited:
            queue = [node]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                queue.extend(current.nodes - visited)
        i += 1
        print(i)
    return visited


def write_graph_to_csv(filename, graph):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for node in graph.list_node:
            writer.writerow([f'{node.data},', ','.join(str(n.data) for n in node.nodes)])

graph = Graph().create_connected_graph(100, 10)
# graph.print()

# dfs = dfs(graph, 0)
# print(dfs, sep='\n')
# print(len(dfs))
#
# bfs = bfs(graph, graph.list_node[0])
# print(*bfs, sep='\n')
# print(len(bfs))

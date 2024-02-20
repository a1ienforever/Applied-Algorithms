import csv
from collections import deque
from tqdm import tqdm

from lb1.RandomGraph import Graph, Cluster, OrientedGraph




def dfs(graph, start_node):
    visited = list()
    stack = [start_node]
    progress_bar = tqdm(total=len(graph))

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
            progress_bar.update()

    progress_bar.close()
    print(len(visited), len(graph))
    return visited


def bfs(graph, start_node):
    visited = list()
    queue = deque([start_node])
    progress_bar = tqdm(total=len(graph))

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            progress_bar.update()

    progress_bar.close()
    return visited


# def write_graph_to_csv(filename, graph):
#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=' ')
#         for node in graph.list_node:
#             writer.writerow([f'{node.data},', ','.join(str(n.data) for n in node.nodes)])


graph = Graph().create_connected_graph(100, 10)
# graph.print()

# dfs = dfs(graph, 0)
# print(dfs, sep='\n')
# print(len(dfs))
#
# bfs = bfs(graph, graph.list_node[0])
# print(*bfs, sep='\n')
# print(len(bfs))

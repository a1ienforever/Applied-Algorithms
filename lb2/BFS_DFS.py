import csv
from collections import deque
from tqdm import tqdm
from collections import defaultdict

from lb1.RandomGraph import Graph, Cluster, OrientedGraph


def dfs(graph, start_node, progress_bar):
    visited = set()
    passed = list()
    stack = [start_node]
    graph = defaultdict(list, graph)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            passed.append(node)
            stack.extend(reversed(graph[node]))
            progress_bar.update(1)

    # print(len(visited), len(graph))
    return passed


def bfs(graph, start_node, progress_bar):
    visited = set()
    passed = list()
    queue = deque([start_node])
    graph = defaultdict(list, graph)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            passed.append(node)
            queue.extend(graph[node])
            progress_bar.update()

    return passed

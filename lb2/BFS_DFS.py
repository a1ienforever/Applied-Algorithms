import csv
from collections import deque
from tqdm import tqdm
from collections import defaultdict

from lb1.RandomGraph import Graph, Cluster, OrientedGraph

def dfs_iterative_return(graphs, start_node):
    all_visited = []
    for i, graph in enumerate(graphs, start=1):
        visited = set()
        stack = []
        visited_order = []
        for start_vertex in graph:
            if start_vertex not in visited:
                stack.append(start_node)
                while stack:
                    current_vertex = stack.pop()
                    if current_vertex not in visited:
                        visited_order.append(current_vertex)
                        visited.add(current_vertex)
                        stack.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)
        all_visited.append(visited_order)
    return all_visited

def bfs(graphs, start_node):
    all_visited = []
    for i, graph in enumerate(graphs, start=1):
        visited = set()
        visited_order = []
        for start_vertex in graph:
            if start_vertex not in visited:
                queue = deque([start_node])
                while queue:
                    current_vertex = queue.popleft()
                    if current_vertex not in visited:
                        visited_order.append(current_vertex)
                        visited.add(current_vertex)
                        queue.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)
        all_visited.append(visited_order)
    return all_visited
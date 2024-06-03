import random
import csv
import tkinter as tk
from tkinter import messagebox

def generate_graph(n, avg_connections, source, directed=False, connected=False):
    graph_data = {}

    connections = int((avg_connections * n) / 2)
    created_connections = 0

    while connections > created_connections:
        top1 = random.randint(1, n)
        top2 = random.randint(1, n)

        if top1 != top2:
            # Проверяем, существует ли уже ребро между вершинами
            edge_exists = False
            for neighbor, weight in graph_data.get(top1, []):
                if neighbor == top2:
                    edge_exists = True
                    break

            if not edge_exists:
                weight = random.randint(1, 10)  # Random weight for the edge
                if top1 not in graph_data:
                    graph_data[top1] = []
                if top2 not in graph_data:
                    graph_data[top2] = []
                graph_data[top1].append((top2, weight))
                if not directed:
                    graph_data[top2].append((top1, weight))
                created_connections += 1

    if connected:
        if not is_connected(graph_data, n):
            # Add additional edges to make the graph connected
            for i in range(1, n):
                if i not in graph_data:
                    graph_data[i] = []
                if i + 1 not in graph_data:
                    graph_data[i + 1] = []
                weight = random.randint(1, 10)  # Random weight for the edge
                graph_data[i].append((i + 1, weight))
                if not directed:
                    graph_data[i + 1].append((i, weight))
            created_connections += n - 1  # Update the total number of connections

    with open('random_graph.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for node, connections in graph_data.items():
            for neighbor, weight in connections:
                writer.writerow([node, neighbor, weight])

    return graph_data

def is_connected(graph_data, n):
    visited = set()
    queue = [1]  # Start from node 1

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            if node in graph_data:
                queue.extend(neighbor for neighbor, _ in graph_data[node])

    return len(visited) == n

if __name__ == '__main__':
    n = 2000
    avg_connections = 10
    source = 1
    directed = False
    connected = True

    graph_data = generate_graph(n, avg_connections, source, directed, connected)

    print("Граф успешно  сгенерирован")


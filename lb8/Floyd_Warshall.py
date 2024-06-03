import csv
import numpy as np
from tqdm import tqdm as pb
import time


def read_file(file_path):
    adjacency_list = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'r') as data:
        for line in data.readlines():
            row = line.rstrip()
            adjacency_list.append([int(x) for x in row.split(',')])
    return adjacency_list


def create_graph(file_name):
    adjacency_list = read_file(file_name)
    maxi = max(node[0] for node in adjacency_list) + 1
    graph = [{} for _ in range(maxi)]
    for node in adjacency_list:
        graph[node[0]][node[1]] = node[2]
    return graph


def create_matrix(file_name):
    inf = np.inf
    graph = create_graph(file_name)
    n = len(graph)
    m = inf * np.ones((n, n))
    t = np.zeros((n, n), dtype=int)
    np.fill_diagonal(m, 0)
    for i in range(n):
        for j, w in graph[i].items():
            m[i, j] = w
            t[i, j] = j + 1
    return m, t


def floyd_warshall(data):
    m = data[0]
    t = data[1]
    n = m.shape[0]

    predecessors = np.zeros((n, n), dtype=int) - 1  # Матрица предшественников, изначально заполненная -1

    pbar = pb(total=n)
    pbar.set_description("\033[35m" + "Floyd-Warshall" + "\033[35m")
    for i in range(n):
        m_ = np.add.outer(m[:, i], m[i, :])
        mask = m_ < m
        t = np.where(mask, i + 1, t)
        predecessors[mask] = i
        m = np.where(mask, m_, m)
        pbar.update(1)
    pbar.close()

    return t, predecessors


def write_result_to_csv(filename, shortest_paths, predecessors):
    n = shortest_paths.shape[0]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Shortest Paths'])
        for row in shortest_paths:
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(['Predecessors'])
        for i in range(n):
            writer.writerow(predecessors[i])




if __name__ == '__main__':
    data = create_matrix('C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb8\\graph.csv')
    timer = time.time()
    t, predecessors = floyd_warshall(data)
    timer1 = time.time() - timer
    write_result_to_csv('output.csv', t, predecessors)
    print(f"Время выполнения: {timer1}")
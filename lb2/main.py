import concurrent.futures
import csv

from concurrent.futures import ThreadPoolExecutor

from GraphReader import GraphReader
from lb2.BFS_DFS import dfs_iterative_return, bfs
from tqdm import tqdm



def read_edges_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        edges = [(int(row[0]), int(row[1])) for row in reader]

        return edges


def edges_to_adjacency_list(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph


def write_graph_to_csv(filename, result):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['bfs'])

        for i in range(len(result[0].result())):
            writer.writerow([result[0].result()[i]])
        writer.writerow(['dfs'])
        for i in range(len(result[1].result())):
            writer.writerow([result[1].result()[i]])

def main():

    gr = GraphReader()
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\graph1.csv'
    graph = gr.read_graph_from_csv(path)
    print(graph)
    progress_bar = tqdm(total=2 * len(graph), desc='bfs and dfs')

    with ThreadPoolExecutor() as executor:
        result = [
            executor.submit(bfs, graph, 1, progress_bar),
            executor.submit(dfs_iterative_return, graph, 1, progress_bar)
        ]
        concurrent.futures.wait(result)

    write_graph_to_csv('bfs_and_dfs.csv', result)
    print("bfs:", len(result[0].result()))
    print("dfs:", len(result[1].result()))
    progress_bar.close()




if __name__ == '__main__':
    main()

import csv

from lb1.RandomGraph import Graph, OrientedGraph, Cluster
from lb2.BFS_DFS import dfs, bfs
from tqdm import tqdm





def read_edges_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # skip header row
        edges = [(int(row[0]), int(row[1])) for row in tqdm(reader)]

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




def main():
    # graph = Graph().create_connected_graph(75000, 40)
    # dfs(graph)
    # # bfs(graph, graph.list_node[0])
    # write_graph_to_csv('dfs.csv', dfs(graph))
    # # write_graph_to_csv('bfs.csv', bfs(graph, graph.list_node[0]))
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\graph.csv'
    edges = read_edges_from_csv(path)
    graph = edges_to_adjacency_list(edges)

    print(*set(graph), sep='\n')
    print(len(set(graph)))
    ddfs = dfs(graph, 2)
    print(*ddfs)
    # print(len(ddfs))
    #
    # bbfs = bfs(graph, 2)
    # # print(*bbfs)



if __name__ == '__main__':
    main()

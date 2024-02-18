import csv

from lb1.RandomGraph import Graph, OrientedGraph, Cluster
from lb2.BFS_DFS import dfs, bfs






def read_edges_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # skip header row
        edges = [(int(row[0]), int(row[1])) for row in reader]

    # invert the edges into an adjacent list
    adj_list = {}
    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append(v)
        if v not in adj_list:
            adj_list[v] = []
        adj_list[v].append(u)

    return adj_list




def main():
    # graph = Graph().create_connected_graph(75000, 40)
    # dfs(graph)
    # # bfs(graph, graph.list_node[0])
    # write_graph_to_csv('dfs.csv', dfs(graph))
    # # write_graph_to_csv('bfs.csv', bfs(graph, graph.list_node[0]))
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\graph.csv'
    graph = read_edges_from_csv(path)
    print(graph, sep='\n')
    ddfs = dfs(graph, 2)
    print(*ddfs)

    bbfs = bfs(graph, 2)
    print(*bbfs)



if __name__ == '__main__':
    main()

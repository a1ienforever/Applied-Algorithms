import csv

from lb1.RandomGraph import Graph, OrientedGraph, Cluster
from lb2.BFS_DFS import dfs


# from lb2.BFS_DFS import dfs, bfs


def write_graph_to_csv(filename, graph):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for node in graph:
            writer.writerow([f'{node.data},', ','.join(str(n.data) for n in node.nodes)])

#TODO заново реалзовать считывание с CSV файла
def read_graph_from_file(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            node, *neighbors = map(int, line.strip().split(': ')[1].split(','))
            graph[node] = neighbors
    return graph





def main():
    # graph = Graph().create_connected_graph(75000, 40)
    # dfs(graph)
    # # bfs(graph, graph.list_node[0])
    # write_graph_to_csv('dfs.csv', dfs(graph))
    # # write_graph_to_csv('bfs.csv', bfs(graph, graph.list_node[0]))
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb1\\graph.csv'
    graph = read_graph_from_file(path)
    print(graph, sep='\n')
    # dfs(graph, 3)
    # write_graph_to_csv('dfs.csv', dfs(graph, 3))


if __name__ == '__main__':
    main()

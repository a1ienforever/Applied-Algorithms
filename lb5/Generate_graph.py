import csv
import random
import time
from tqdm import tqdm
import configparser


class Vertex:
    def __init__(self, data=None):
        self.neighbors = {}  # Словарь для хранения соседей и их весов
        self.data = data

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def __str__(self):
        neighbors_str = ';'.join([f"{neighbor.data}:{weight}" for neighbor, weight in self.neighbors.items()])
        return f"{self.data} ; {neighbors_str}"


class Connect_Graph:
    def __init__(self):
        self.list_node = []
        self.sum_conn = 0
        self.qvertex = 0
        self.average = 0

    def create_connected_graph(self, num_vertices, avg_connectivity):
        self.qvertex = num_vertices
        self.average = avg_connectivity
        pbar = tqdm(total=self.qvertex, desc='Graph generate')
        for i in range(0, num_vertices):
            ver = Vertex(i)
            self.list_node.append(ver)

        for node in self.list_node[:len(self.list_node)-1]:
            # pbar.update(1)
            max_edges = avg_connectivity

            # Создание хотя бы одного ребра для текущей вершины
            if max_edges > 0:
                rand_conn_num = random.randint(max_edges - 1, max_edges + 1)
                # self.sum_conn += rand_conn_num

                connected_nodes = set()
                connected_nodes.add(self.list_node[0])


                for _ in range(rand_conn_num):
                    k = 0
                    while True:
                        connected_node = random.choice(self.list_node)
                        k += 1
                        if connected_node != node and connected_node not in connected_nodes:
                            node.add_neighbor(connected_node, random.randint(2, 10))
                            break
                        if k > self.qvertex:
                            _ = rand_conn_num
                            break

                    connected_nodes.add(connected_node)
                pbar.update(1)
            else:
                pbar.update(1)
        pbar.close()
        return self

    def average_connectivity(self):
        suma = 0
        pbar = tqdm(total=self.qvertex, desc='Average')
        for i in self.list_node:
            pbar.update(1)
            suma += len(i.neighbors)
        pbar.close()
        return suma / len(self.list_node)

    def graph_in_csv(self, filename, graph, type):
        pbar = tqdm(total=self.qvertex, desc='Write to csv')
        if type == 'csv':
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                # writer.writerow(f'Vertexs;ribs')
                for node in graph.list_node:
                    pbar.update(1)
                    writer.writerow([f'{node.data};',
                                     ';'.join(
                                         f'{n[0].data}/{n[1]}' for n in
                                         node.neighbors.items())])
            pbar.close()


def main():  # Основная функция программы
    config = configparser.ConfigParser()
    config.read('graph.ini')
    graph = Connect_Graph()  # Создание объекта класса Graph
    graph1 = graph.create_connected_graph(int(config["IN"]["qvertex"]), int(config["IN"]["average"]))
    average = graph.average_connectivity()
    graph.graph_in_csv(f'graph.csv', graph1, 'csv')
    print(f"Average: {average}")


if __name__ == "__main__":  # Проверка, что скрипт запускается напрямую
    timer = time.time()  # Получение текущего врем
    main()
    print(f'Execution time: {round(time.time() - timer, 2)} s')

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
        neighbor.neighbors[self] = weight  # Добавляем взаимную связь с весом к соседней вершине

    def __str__(self):
        neighbors_str = ';'.join([f"{neighbor.data}:{weight}" for neighbor, weight in self.neighbors.items()])
        return f"{self.data} ; {neighbors_str}"


class Connect_Graph:  # Определение класса Graph
    def __init__(self):  # Инициализация класса
        self.list_node = []  # Создание списка для хранения узлов
        self.list_vertex = set()
        self.sum_conn = 0  # Инициализация счетчика связей
        self.qvertex = 0
        self.average = 0

    def create_connected_graph(self, num_vertices, avg_connectivity):
        self.qvertex = num_vertices
        self.average = avg_connectivity
        pbar = tqdm(total=self.qvertex)
        pbar.set_description("\033[35m" + "graph generation" + "\033[35m")
        for i in range(0, num_vertices):
            ver = Vertex(i)
            self.list_node.append(ver)
            self.list_vertex.add(ver)

        for node in self.list_node:
            pbar.update(1)
            max_edges = avg_connectivity

            # Создание хотя бы одного ребра для текущей вершины
            if max_edges > 0:
                rand_conn_num = random.randint(max_edges - 1, max_edges + 1)
                flag = True
                # self.sum_conn += rand_conn_num

                connected_nodes = set()
                for _ in range(rand_conn_num):
                    k = 0
                    while True:
                        connected_node = random.choice(self.list_node)
                        k += 1
                        if ((connected_node != node) and (connected_node not in connected_nodes)
                                and ((int(node.data) % 2 == 0 and int(connected_node.data) % 2 != 0)
                                     or (int(node.data) % 2 != 0 and int(connected_node.data) % 2 == 0))):
                            break
                        if k > self.qvertex:
                            _ = rand_conn_num
                            flag = False
                            break
                    if flag:
                        node.add_neighbor(connected_node, random.randint(1, 50))

                    if len(connected_node.neighbors) == avg_connectivity + 1:
                        self.list_node.pop(self.list_node.index(connected_node))
                        pbar.update(1)
                    connected_nodes.add(connected_node)
                self.list_node.pop(self.list_node.index(node))
                pbar.update(1)
            else:
                self.list_node.pop(self.list_node.index(node))
                pbar.update(1)
        pbar.close()
        return self

    def average_connectivity(self):
        suma = 0
        pbar = tqdm(total=self.qvertex)
        pbar.set_description("\033[35m" + "calculating the average" + "\033[35m")
        for i in self.list_vertex:
            pbar.update(1)
            if len(i.neighbors) <= 1:
                for _ in range(2):
                    n = random.choice(list(self.list_vertex))
                    if (n.data == i.data or ((int(n.data) % 2 == 0 and int(i.data) % 2 == 0)
                                              or (int(n.data) % 2 != 0 and int(i.data) % 2 != 0))):
                        _ -= 1
                    else:
                        i.add_neighbor(n, random.randint(1, 50))
                        suma += 2
            suma += len(i.neighbors)
        pbar.close()
        return suma / len(self.list_vertex)

    def graph_in_csv(self, filename, graph, type):  # Метод для записи графа в CSV файл
        pbar = tqdm(total=self.qvertex)
        pbar.set_description("\033[35m" + "Writing to csv" + "\033[35m")
        if type == 'csv':
            with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                # writer.writerow(f'Vertexs;ribs')  # Запись заголовков
                for node in sorted(graph.list_vertex, key=lambda x: x.data):  # Перебор всех узлов графа
                    pbar.update(1)
                    writer.writerow([f'{node.data};',
                                     ';'.join(
                                         f'{n[0].data}!{n[1]}' for n in
                                         node.neighbors.items())])  # Запись данных узла и его смежных узлов
            pbar.close()
        else:
            with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                for node in graph.list_vertex:  # Перебор всех узлов графа
                    writer.writerow(
                        [f'{str(node.data)[0:len(str(node.data))]}:', ','.join(str(n.data) for n in node.vertexs)])




def main():  # Основная функция программы
    config = configparser.ConfigParser()
    path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb6\\config.ini'
    config.read(path)
    graph = Connect_Graph()  # Создание объекта класса Graph
    graph1 = graph.create_connected_graph(int(config["IN"]["qvertex"]), int(config["IN"]["average"]))
    average = graph.average_connectivity()
    graph.graph_in_csv(f'graph.csv', graph1, 'csv')
    print(f"Average: {average}")



if __name__ == "__main__":  # Проверка, что скрипт запускается напрямую
    timer = time.time()  # Получение текущего врем
    main()
    print(f'Execution time: {round(time.time() - timer, 2)} s')

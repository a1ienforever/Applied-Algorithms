import csv
import random
import time
from tqdm import tqdm
import configparser
import threading


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




class Connect_Graph:
    def __init__(self):
        self.list_node = []
        self.list_vertex = set()
        self.sum_conn = 0
        self.qvertex = 0
        self.average = 0

    def create_connected_graph(self, num_vertices, avg_connectivity):
        self.qvertex = num_vertices
        self.average = avg_connectivity
        pbar = tqdm(total=self.qvertex, desc='graph generation')
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
                # self.sum_conn += rand_conn_num

                connected_nodes = set()
                for _ in range(rand_conn_num):
                    k = 0
                    while True:
                        connected_node = random.choice(self.list_node)
                        k += 1
                        if connected_node != node and connected_node not in connected_nodes:
                            break
                        if k > self.qvertex:
                            _ = rand_conn_num
                            break

                    node.add_neighbor(connected_node, random.randint(1, 5))
                    # connected_node.vertexs.add(node)
                    # self.sum_conn += 2
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
        pbar = tqdm(total=self.qvertex, desc='average')
        for i in self.list_vertex:
            pbar.update(1)
            if len(i.neighbors) <= 1:
                for _ in range(2):
                    n = random.choice(list(self.list_vertex)[list(self.list_vertex).index(i):])
                    i.add_neighbor(n, random.randint(1, 10))
                    suma += 2
            suma += len(i.neighbors)
        pbar.close()
        return suma / len(self.list_vertex)

    def graph_in_csv(self, filename, graph, type):  # Метод для записи графа в CSV файл
        pbar = tqdm(total=self.qvertex, desc='writing to csv')
        if type == 'csv':
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                writer.writerow(f'Vertexs;ribs')  # Запись заголовков
                for node in graph.list_vertex:  # Перебор всех узлов графа
                    pbar.update(1)
                    writer.writerow([f'{node.data};',
                                     ';'.join(
                                         f'{n[0].data}!{n[1]}' for n in node.neighbors.items())])  # Запись данных узла и его смежных узлов
            pbar.close()
        else:
            with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                for node in graph.list_vertex:  # Перебор всех узлов графа
                    writer.writerow(
                        [f'{str(node.data)[0:len(str(node.data))]}:', ','.join(str(n.data) for n in node.vertexs)])


class Disconnect_Graph:
    def __init__(self, qvertex):
        self.main_graph = []
        self.qvertex = qvertex
        self.pbar = tqdm(total=self.qvertex)
        self.pbar.set_description("\033[35m" + "graph generation" + "\033[35m")

    def delimiter(self, qvertex: int, average: int):  # Обратите внимание на параметр self
        self.qvertex = qvertex
        delitel = []
        if self.qvertex - average < self.qvertex // 2:
            n = random.randint(2, 10)
            delitel.append((0, self.qvertex - n, self.qvertex - 1, average))
            delitel.append((self.qvertex - n + 1, self.qvertex + 1, (self.qvertex - n + 1) - (self.qvertex + 1), n))
            for i in delitel:
                list_1 = self.generate_disconnect_graph(i[0], i[1], i[2], i[3])
                self.main_graph += list_1
            self.average_connectivity()
        elif self.qvertex - average == self.qvertex // 2:
            delitel.append((0, (self.qvertex - self.qvertex // 2) - 1, self.qvertex // 2, average))
            delitel.append(((self.qvertex - self.qvertex // 2), self.qvertex, self.qvertex // 2, average))
            for i in delitel:
                list_1 = self.generate_disconnect_graph(i[0], i[1], i[2], i[3])
                self.main_graph += list_1
            self.average_connectivity()
        else:
            start = 0
            finish = 0
            for i in range(average):
                if i == 0:
                    start = 0
                    finish = int(self.qvertex / average)
                    delitel.append((start, finish, finish - start, average))
                    start += int(self.qvertex / average)
                    finish += int(self.qvertex / average)
                elif i < average - 1:
                    delitel.append((start, finish, finish - start, average))
                    start += int(self.qvertex / average)
                    finish += int(self.qvertex / average)
                else:
                    finish = self.qvertex
                    delitel.append((start, finish, finish - start, average))
            for j in delitel:
                thr = threading.Thread(target=self.generate_disconnect_graph, args=(j[0], j[1], j[2], j[3],))
                thr.start()
                if j == delitel[len(delitel) - 1]:
                    thr.join()
        self.pbar.close()

    def generate_disconnect_graph(self, start, finish, qvertex, average):
        list_node = []
        list_vertex = set()
        for i in range(start, finish):
            var = Vertex(i)
            list_node.append(var)
            list_vertex.add(var)

        for node in list_node:
            self.pbar.update(1)
            max_edges = average

            # Создание хотя бы одного ребра для текущей вершины
            if max_edges > 0:
                rand_conn_num = random.randint(max_edges - 1, max_edges + 1)
                # self.sum_conn += rand_conn_num

                connected_nodes = set()
                for _ in range(rand_conn_num):
                    k = 0
                    while True:
                        connected_node = random.choice(list_node)
                        k += 1
                        if connected_node != node and connected_node not in connected_nodes:
                            break
                        if k > qvertex:
                            _ = rand_conn_num
                            break
                    node.add_neighbor(connected_node, random.randint(1, 10))

                    # self.sum_conn += 2
                    if len(connected_node.neighbors) == average + 1:
                        list_node.pop(list_node.index(connected_node))
                        self.pbar.update(1)
                    connected_nodes.add(connected_node)
                list_node.pop(list_node.index(node))
                self.pbar.update(1)
            else:
                list_node.pop(list_node.index(node))
                self.pbar.update(1)
        self.main_graph += list_vertex
        return True

    def average_connectivity(self):
        suma = 0
        pbar = tqdm(total=len(self.main_graph))
        pbar.set_description("\033[35m" + "calculating the average" + "\033[35m")
        for i in self.main_graph:
            if len(i.neighbors) <= 1:
                for _ in range(2):
                    n = random.choice(list(self.main_graph))
                    i.add_neighbor(n, random.randint(1, 10))
                    suma += 2
            suma += len(i.neighbors)
            pbar.update(1)
        pbar.close()
        return suma / len(self.main_graph)

    def graph_in_csv(self, filename, type):  # Метод для записи графа в CSV файл
        pbar = tqdm(total=self.qvertex, desc='writing to csv')
        if type == 'csv':
            with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                # writer.writerow(f'Vertexs;ribs')  # Запись заголовков
                for node in self.main_graph:  # Перебор всех узлов графа
                    pbar.update(1)
                    writer.writerow([f'{node.data};',
                                     ';'.join(
                                         f'{n[0].data}!{n[1]}' for n in node.neighbors.items())])  # Запись данных узла и его смежных узлов
            pbar.close()
        else:
            with open(filename, 'w', newline='') as csvfile:  # Открытие файла для записи
                writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
                for node in self.main_graph:  # Перебор всех узлов графа
                    writer.writerow(
                        [f'{str(node.data)[0:len(str(node.data))]}:', ','.join(str(n.data) for n in node.vertexs)])


def main():  # Основная функция программы
    config = configparser.ConfigParser()
    config.read('graph.ini')
    if int(config["IN"]["condis"]) == 1:
        graph = Connect_Graph()  # Создание объекта класса Graph
        graph1 = graph.create_connected_graph(int(config["IN"]["qvertex"]), int(config["IN"]["average"]))
        print(len(graph1.list_vertex))
        average = graph.average_connectivity()
        graph.graph_in_csv(f'graph.csv', graph1, 'csv')
        # print(f"Average: {average}")
    else:
        graph = Disconnect_Graph(int(config["IN"]["qvertex"]))
        graph.delimiter(qvertex=int(config["IN"]["qvertex"]), average=int(config["IN"]["average"]))
        graph.graph_in_csv(f'graph.csv', 'csv')
        # result = graph.average_connectivity()
        # print(f'Average: {result}')


if __name__ == "__main__":
    timer = time.time()
    main()
    print(f'Execution time: {round(time.time() - timer, 2)} s')

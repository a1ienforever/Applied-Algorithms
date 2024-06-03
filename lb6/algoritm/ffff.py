import time
from queue import Queue
import csv
import numpy as np
from tqdm import tqdm as pb

INF = 2147483647
NIL = 0


class Graph(object):
    def __init__(self, m, n):
        self.__m = m
        self.__n = n
        self.__adj = {u: [] for u in range(1, m + 1)}

    def addEdge(self, u, v, weight):
        self.__adj[u].append((v, weight))

    def bfs(self):
        Q = Queue()
        for u in range(1, self.__m + 1):
            if self.__pairU[u] == NIL:
                self.__dist[u] = 0
                Q.put(u)
            else:
                self.__dist[u] = INF
        self.__dist[NIL] = INF
        while not Q.empty():
            u = Q.get()
            if self.__dist[u] < self.__dist[NIL]:
                for v, weight in self.__adj[u]:
                    if self.__dist[self.__pairV[v]] == INF:
                        self.__dist[self.__pairV[v]] = self.__dist[u] + weight
                        Q.put(self.__pairV[v])
        return self.__dist[NIL] != INF

    def dfs(self, u):
        if u != NIL:
            for v, weight in self.__adj[u]:
                if self.__dist[self.__pairV[v]] == self.__dist[u] + weight:
                    if self.dfs(self.__pairV[v]):
                        self.__pairV[v] = u
                        self.__pairU[u] = v
                        return True
            self.__dist[u] = INF
            return False
        return True

    def hopcroftKarp(self):
        self.__pairU = [0] * (self.__m + 1)
        self.__pairV = [0] * (self.__n + 1)
        self.__dist = [0] * (self.__m + 1)
        result = 0
        matching = []

        pbar = pb(total=self.__m, desc='hungarian_algorithm')

        while self.bfs():
            for u in range(1, self.__m + 1):
                pbar.update(1)
                if self.__pairU[u] == NIL and self.dfs(u):
                    result += 1
        pbar.close()
        for u in range(1, self.__m + 1):
            if self.__pairU[u] != NIL:
                v = self.__pairU[u]
                matching.append((u, v, self.getEdgeWeight(u, v)))

        return matching

    def getEdgeWeight(self, u, v):
        for neighbor, weight in self.__adj[u]:
            if neighbor == v:
                return weight
        return None


def read_file(file_path):
    global g
    with open(file_path, 'r') as file:
        lines = file.readlines()

    pbar = pb(total=len(lines), desc='Read file')

    # Читаем данные из CSV файла
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            pbar.update(1)
            node = int(row[0]) + 1
            edges = row[1:]
            for edge in edges:
                target, weight = map(int, edge.split('!'))
                target += 1
                g.addEdge(node, target, weight)
    pbar.close()


def write_csv(matrix):  # Метод для записи графа в CSV файл
    pbar = pb(total=len(matrix), desc='Writing to csv')
    with open("result.csv", 'w', newline='') as csvfile:  # Открытие файла для записи
        writer = csv.writer(csvfile, delimiter=' ')  # Создание объекта для записи CSV
        for node in matrix:  # Перебор всех узлов графа
            pbar.update(1)
            writer.writerow([f'{node[0]};{node[1]};{node[2]}'])  # Запись данных узла и его смежных узлов
    pbar.close()


# Пример использования
if __name__ == "__main__":
    file_path = 'C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb6\\graph.csv'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    g = None
    g = Graph(len(lines), len(lines))
    read_file(file_path)
    res = g.hopcroftKarp()
    result = []
    for i in res[0::2]:
        i = list(i)
        i[0] = i[0] - 1
        i[1] = i[1] - 1
        i = tuple(i)
        result.append(i)
    write_csv(result)

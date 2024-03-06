import csv


class GraphReader:

    def read_graph_from_csv(self, filename):
        graph = []
        adjacency_lists = {}
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            i = 0
            for row in reader:
                if row[0] in adjacency_lists:
                    adjacency_lists = {int(k): v for k, v in adjacency_lists.items() if v}

                    graph.append(adjacency_lists)
                    adjacency_lists = {}
                vertex = row[0]
                neighbors = [int(neighbor) for neighbor in row[1:]]
                i += 1
                adjacency_lists[vertex] = neighbors

        return graph




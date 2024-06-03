import csv
from tqdm import tqdm
from GraphReader import GraphReader


def edge_coloring(graph):
    def get_edge_color(edge_colors, edge):
        return edge_colors.get(edge, None)

    def set_edge_color(edge_colors, edge, color):
        edge_colors[edge] = color

    edges = set()
    for node in graph:
        for neighbor in graph[node]:
            edge = tuple(sorted((node, neighbor)))
            if edge not in edges:
                edges.add(edge)
    edges = list(edges)

    max_degree = max(len(neighbors) for neighbors in graph.values())
    color_range = list(range(1, max_degree + 2))


    edge_colors = {}
    for edge in edges:

        node, neighbor = edge
        available_colors = set(color_range)
        # Убираем цвета, уже использованные соседними рёбрами
        for adj in graph[node]:
            used_color = get_edge_color(edge_colors, tuple(sorted((node, adj))))
            if used_color in available_colors:
                available_colors.remove(used_color)
        for adj in graph[neighbor]:
            used_color = get_edge_color(edge_colors, tuple(sorted((neighbor, adj))))
            if used_color in available_colors:
                available_colors.remove(used_color)
        # Выбираем первый доступный цвет
        chosen_color = min(available_colors)
        set_edge_color(edge_colors, edge, chosen_color)

    return edge_colors

def check_uniqueness_of_colors(edge_colors):
    color_usage = {}
    for edge, color in edge_colors.items():
        if color in color_usage:
            color_usage[color].append(edge)
        else:
            color_usage[color] = [edge]
    for edges in color_usage.values():
        if len(edges) > 1:
            return False
    return True


def convert_to_colored_adjacency_list(graph, edge_colors):
    colored_graph = {}
    for node in graph:
        colored_graph[node] = []
        for neighbor in graph[node]:
            edge = tuple(sorted((node, neighbor)))
            color = edge_colors.get(edge)
            colored_graph[node].append((neighbor, color))
    return colored_graph


def write_colored_graph_to_csv(colored_graph, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for node, neighbors in colored_graph.items():
            row = [node]
            for neighbor, color in neighbors:
                row.append(f"{neighbor},{color}")
            writer.writerow(row)





def check_correctness(graph, edge_colors):
    for node in graph:
        used_colors = set()
        for neighbor in graph[node]:
            edge = tuple(sorted((node, neighbor)))
            color = edge_colors.get(edge)
            if color is None:
                print(f"Error: {edge} не имеет цвета.")
                return False
            if color in used_colors:
                print(f"Error: Смежные ребра узла {node} имеют одинаковый цвет {color}.")
                return False
            used_colors.add(color)
    return True


# Пример использования функции
if __name__ == '__main__':
    path = "C:\\Users\\artyo\\PycharmProjects\\Applied Algorithms\\lb9\\graph.csv"
    graph_data = GraphReader().read_graph_from_csv(path)

    edge_colors = edge_coloring(graph_data)

    is_unique = check_uniqueness_of_colors(edge_colors)
    is_correct = check_correctness(graph_data[0], edge_colors)

    print("Корректность раскрашивания:", is_correct)

    if is_correct:
        colored_adjacency_list = convert_to_colored_adjacency_list(graph_data[0], edge_colors)
        write_colored_graph_to_csv(colored_adjacency_list, 'colored_graph.csv')
        print("Colored graph has been written to 'colored_graph.csv'")
    else:
        print("There was an error in coloring the graph.")

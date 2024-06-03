import csv
import heapq

def dijkstra(nodes, lines, start, end):
    num_nodes = len(nodes)
    unexplored = {node: {'time': float('inf'), 'path': []} for node in nodes}
    unexplored[start]['time'] = 0  # Устанавливаем стартовую вершину

    heap = [(0, start)]
    visited = set()

    while heap:
        current_time, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            break

        for next_node, time in lines[current_node].items():
            new_time = current_time + time
            if new_time < unexplored[next_node]['time']:
                unexplored[next_node]['time'] = new_time
                unexplored[next_node]['path'] = unexplored[current_node]['path'] + [next_node]
                heapq.heappush(heap, (new_time, next_node))

    return unexplored

def read_csv(filename):
    nodes = set()
    lines = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nodes.add(row[0])
            nodes.add(row[1])
            if row[0] not in lines:
                lines[row[0]] = {}
            lines[row[0]][row[1]] = int(row[2])
    return nodes, lines

def write_csv(filename, result, end):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Start', 'Path', 'Shortest Time'])
        shortest_time = result[end]['time']
        shortest_path = result[end]['path']
        # writer.writerow([shortest_path[0], ' ~ '.join(shortest_path), shortest_time])
        for i in shortest_path:
            writer.writerow([i])
        print("Start", shortest_path[0])
        print("Path", *shortest_path)
        print(shortest_time)

def main(input_file, output_file, end):
    nodes, lines = read_csv(input_file)
    result = dijkstra(nodes, lines, "1", end)
    write_csv(output_file, result, end)

if __name__ == "__main__":
    end_node = input("Введите конечную вершину стока: ")
    main("random_graph.csv", "shortest_path_result.csv", end_node)

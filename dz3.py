import heapq  # Імпортуємо бібліотеку heapq для роботи з бінарною купою (пірамідою)

class Graph:
    def __init__(self):
        self.edges = {}  # Словник для зберігання ребер графа та їх ваги

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))  # Додаємо ребро та його вагу

def dijkstra(graph, start):
    # Ініціалізуємо пріоритетну чергу
    priority_queue = []  # Використовуємо бінарну купу для оптимізації
    heapq.heappush(priority_queue, (0, start))  # Додаємо початкову вершину з вагою 0

    # Словник для зберігання найкоротших шляхів до кожної вершини
    shortest_path = {start: (None, 0)}  # Початковий шлях - None, вага - 0

    while priority_queue:
        current_weight, current_node = heapq.heappop(priority_queue)

        # Перевіряємо, чи вершина вже була відвідана коротшим шляхом
        if current_weight > shortest_path[current_node][1]:
            continue

        for neighbor, weight in graph.edges.get(current_node, []):
            distance = current_weight + weight
            if neighbor not in shortest_path or distance < shortest_path[neighbor][1]:
                shortest_path[neighbor] = (current_node, distance)
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_path

def construct_path(shortest_path, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_path[current_node][0]
        current_node = next_node
    path.reverse()
    return path

# Приклад використання:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Виведення найкоротших шляхів від початкової вершини до всіх інших
for node in shortest_paths:
    print(f"Найкоротший шлях з {start_node} до {node}: {construct_path(shortest_paths, start_node, node)} з відстанню {shortest_paths[node][1]}")

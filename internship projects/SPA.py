import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest, weight):
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))      

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example usage:
if __name__ == "__main__":
    city_graph = Graph()

    # Add edges (landmarks and distances)
    city_graph.add_edge("A", "B", 5)
    city_graph.add_edge("A", "C", 10)
    city_graph.add_edge("B", "C", 2)
    city_graph.add_edge("B", "D", 4)
    city_graph.add_edge("C", "D", 7)
    city_graph.add_edge("C", "E", 1)
    city_graph.add_edge("D", "E", 3)

    print("City Graph:")
    city_graph.print_graph()
    
    start_landmark = "A"
    shortest_paths = city_graph.dijkstra(start_landmark)
    print(f"\nShortest paths from {start_landmark}:")
    for landmark, distance in shortest_paths.items():
        print(f"Distance to {landmark}: {distance}")

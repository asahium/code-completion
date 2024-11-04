class Dijkstra():
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.graph = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    def min_distance(self, dist, min_dist_set):
        min_dist = float("inf")
        for target in range(self.vertex_count):
            if min_dist_set[target]:
                continue
            if dist[target] < min_dist:
                min_dist = dist[target]
                min_index = target
        return min_index

    def dijkstra(self, src):
        dist = [float("inf")] * self.vertex_count
        dist[src] = 0
        min_dist_set = [False] * self.vertex_count

        for _ in range(self.vertex_count):
            source = self.min_distance(dist, min_dist_set)

            min_dist_set[source] = True

            for target in range(self.vertex_count):
                if self.graph[source][target] <= 0 or min_dist_set[target]:
                    continue
                if dist[target] > dist[source] + self.graph[source][target]:
                    dist[target] = dist[source] + self.graph[source][target]

        return dist

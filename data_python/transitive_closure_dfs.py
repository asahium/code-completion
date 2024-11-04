class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.vertex_count = vertices

        # default dictionary to store graph
        self.graph = {}

        # To store transitive closure
        self.closure = [[0 for j in range(vertices)] for i in range(vertices)]

    def add_edge(self, source, target):
        if source in self.graph:
            self.graph[source].append(target)
        else:
            self.graph[source] = [target]

    def dfs_util(self, source, target):
        # Mark reachability from source to target as true.
        self.closure[source][target] = 1

        # Find all the vertices reachable through target
        for adjacent in self.graph[target]:
            if self.closure[source][adjacent] == 0:
                self.dfs_util(source, adjacent)

    def transitive_closure(self):
        # Call the recursive helper function to print DFS
        # traversal starting from all vertices one by one
        for i in range(self.vertex_count):
            self.dfs_util(i, i)

        return self.closure

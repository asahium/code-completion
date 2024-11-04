import copy
import math

def maximum_flow_dfs(adjacency_matrix):
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while True:
        min = math.inf
        visited = [0]*len(new_array)
        path = [0]*len(new_array)

        stack = []

        visited[0] = 1
        stack.append(0)

        while len(stack) > 0:
            src = stack.pop()
            for k in range(len(new_array)):
                if new_array[src][k] > 0 and visited[k] == 0:
                    visited[k] = 1
                    stack.append(k)
                    path[k] = src

        if visited[len(new_array) - 1] == 0:
            break

        tmp = len(new_array) - 1

        while tmp != 0:
            if min > new_array[path[tmp]][tmp]:
                min = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        tmp = len(new_array) - 1

        while tmp != 0:
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min

    return total


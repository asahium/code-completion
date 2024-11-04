import copy
import queue
import math

def maximum_flow_bfs(adjacency_matrix):
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while True:
        min_flow = math.inf
        visited = [0]*len(new_array)
        path = [0]*len(new_array)

        bfs = queue.Queue()

        visited[0] = 1
        bfs.put(0)

        while bfs.qsize() > 0:
            src = bfs.get()
            for k in range(len(new_array)):
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src

        if visited[len(new_array) - 1] == 0:
            break

        tmp = len(new_array) - 1

        while tmp != 0:
            if min_flow > new_array[path[tmp]][tmp]:
                min_flow = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        tmp = len(new_array) - 1

        while tmp != 0:
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min_flow
            tmp = path[tmp]

        total = total + min_flow

    return total

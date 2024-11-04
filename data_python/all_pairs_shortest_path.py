import copy

def all_pairs_shortest_path(adjacency_matrix):
    new_array = copy.deepcopy(adjacency_matrix)

    size = len(new_array)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if new_array[i][j] > new_array[i][k] + new_array[k][j]:
                    new_array[i][j] = new_array[i][k] + new_array[k][j]

    return new_array

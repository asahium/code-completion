def linear_search(array, query):
    for i, value in enumerate(array):
        if value == query:
            return i
    return -1

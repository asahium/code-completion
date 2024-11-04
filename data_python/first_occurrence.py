def first_occurrence(array, query):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high-low)//2
        if low == high:
            break
        if array[mid] < query:
            low = mid + 1
        else:
            high = mid
    if array[low] == query:
        return low

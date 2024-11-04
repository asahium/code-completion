def search_insert(array, val):
    low = 0
    high = len(array) - 1
    while low <=  high:
        mid = low + (high - low) // 2
        if val > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

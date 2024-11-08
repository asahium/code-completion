def last_occurrence(array, query):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == query and mid == len(array)-1) or \
           (array[mid] == query and array[mid+1] > query):
            return mid
        if array[mid] <= query:
            low = mid + 1
        else:
            high = mid - 1

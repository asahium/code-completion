def search_rotate(array, val):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == array[mid]:
            return mid

        if array[low] <= array[mid]:
            if array[low] <= val <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] <= val <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

def search_rotate_recur(array, low, high, val):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if val == array[mid]:  
        return mid
    if array[low] <= array[mid]:
        if array[low] <= val <= array[mid]:
            return search_rotate_recur(array, low, mid - 1, val) 
        return search_rotate_recur(array, mid + 1, high, val)  
    if array[mid] <= val <= array[high]:
        return search_rotate_recur(array, mid + 1, high, val) 
    return search_rotate_recur(array, low, mid - 1, val)  

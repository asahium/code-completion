def pancake_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    for cur in range(len(arr), 1, -1):
        index_max = arr.index(max(arr[0:cur]))
        if index_max+1 != cur:
            if index_max != 0:
                arr[:index_max+1] = reversed(arr[:index_max+1])
            arr[:cur] = reversed(arr[:cur])
    return arr

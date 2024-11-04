def counting_sort(arr):
    m = min(arr)
    different = 0
    if m < 0:
        different = -m
        for i in range(len(arr)):
            arr[i] += -m
    k = max(arr)
    temp_arr = [0] * (k + 1)
    for i in range(0, len(arr)):
        temp_arr[arr[i]] = temp_arr[arr[i]] + 1

    for i in range(1, k + 1):
        temp_arr[i] = temp_arr[i] + temp_arr[i - 1]

    result_arr = arr.copy()
    for i in range(len(arr) - 1, -1, -1):
        result_arr[temp_arr[arr[i]] - 1] = arr[i] - different
        temp_arr[arr[i]] = temp_arr[arr[i]] - 1

    return result_arr

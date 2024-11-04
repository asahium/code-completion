from typing import List


def interpolation_search(array: List[int], search_key: int) -> int:
    high = len(array) - 1
    low = 0

    while (low <= high) and (array[low] <= search_key <= array[high]):
        pos = low + int(((search_key - array[low]) *
                         (high - low) / (array[high] - array[low])))

        if array[pos] == search_key:
            return pos

        if array[pos] < search_key:
            low = pos + 1

        else:
            high = pos - 1

    return -1

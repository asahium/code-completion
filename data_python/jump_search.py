import math

def jump_search(arr,target):
    length = len(arr)
    block_size = int(math.sqrt(length))
    block_prev = 0
    block= block_size
    if arr[length - 1] < target:
        return -1
    while block <= length and arr[block - 1] < target:
        block_prev = block
        block += block_size
    while arr[block_prev] < target :
        block_prev += 1
        if block_prev == min(block, length) :
            return -1
    if arr[block_prev] == target :
        return block_prev
    return -1

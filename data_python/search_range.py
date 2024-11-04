def search_range(nums, target):
    low = 0
    high = len(nums) - 1
    # breaks at low == high
    # both pointing to first occurence of target
    while low < high:
        mid = low + (high - low) // 2
        if target <= nums[mid]:
            high = mid
        else:
            low = mid + 1

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            return [low, j]

    return [-1, -1]

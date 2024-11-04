def two_sum(numbers, target):
    for i, number in enumerate(numbers):
        second_val = target - number
        low, high = i+1, len(numbers)-1
        while low <= high:
            mid = low + (high - low) // 2
            if second_val == numbers[mid]:
                return [i + 1, mid + 1]

            if second_val > numbers[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return None

def two_sum1(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i
    return None

def two_sum2(numbers, target):
    left = 0                      # pointer 1 holds from left of array numbers
    right = len(numbers) - 1       # pointer 2 holds from right of array numbers
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum > target:
            right = right - 1
        else:
            left = left + 1

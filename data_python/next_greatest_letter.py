import bisect

def next_greatest_letter(letters, target):
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]

def next_greatest_letter_v1(letters, target):
    if letters[0] > target:
        return letters[0]
    if letters[len(letters) - 1] <= target:
        return letters[0]
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if  letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return letters[left]

def next_greatest_letter_v2(letters, target):
    for index in letters:
        if index > target:
            return index
    return letters[0]

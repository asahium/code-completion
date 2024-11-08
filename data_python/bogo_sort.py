import random

def bogo_sort(arr, simulation=False):
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    
    def is_sorted(arr):
        i = 0
        arr_len = len(arr)
        while i+1 < arr_len:
            if arr[i] > arr[i+1]:
                return False
            i += 1
            

        return True
    while not is_sorted(arr):
        random.shuffle(arr)
        
        if simulation:
            iteration = iteration + 1
            print("iteration",iteration,":",*arr)
            
    return arr

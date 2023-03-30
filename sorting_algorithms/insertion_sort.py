# InsertionSort

def insertion_sort(arr):
    i = 1
    j = i - 1
    while i < len(arr):
        min_ = arr[i]
        while j >= 0 and min_ < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1  # here wil be -1 when we swap 2 and 1
        arr[j + 1] = min_
        i += 1
        j = i - 1
    return arr


print(insertion_sort([2, 1, 9, 76, 4]))

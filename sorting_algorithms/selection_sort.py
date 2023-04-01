# Selection sort
def selection_sort(arr):
    i = 0
    j = i + 1
    while i < len(arr):
        min_ = i
        while j < len(arr):
            if arr[min_] > arr[j]:
                min_ = j
                j += 1
            else:
                j += 1
        if min_ != i:
            arr[min_], arr[i] = arr[i], arr[min_]
        i += 1
        j = i + 1
    return arr


print(selection_sort([5, 1, 76, 2, 43, 23, 84, 4, 0, 59, 12]))


# Reverse Selection
def reverse_selection(arr):
    i = 0
    j = i + 1
    while i < len(arr):
        max_ = i
        while j < len(arr):
            if arr[j] > arr[max_]:
                max_ = j
                j += 1
            else:
                j += 1
        if max_ != i:
            arr[max_], arr[i] = arr[i], arr[max_]
        i += 1
        j = i + 1
    return arr

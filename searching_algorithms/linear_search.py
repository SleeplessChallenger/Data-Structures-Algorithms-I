# Linear search
def search(arr, val):
    for x in range(len(arr)):
        if arr[x] == val:
            return x
    return -1


print(search([2, 5, 1, 6, 9, 10], 5))


# second way
def als_search(arr, val):
    for x in arr:
        if x == val:
            return arr.index(x)
    return -1

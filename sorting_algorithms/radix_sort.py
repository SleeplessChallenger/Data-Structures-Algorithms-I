from math import floor, pow, log10


def radix(array):
    i = 0
    j = 0
    lst = list()
    dct = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    max_dig = most_digits(array)
    while i < max_dig:
        while j < len(array):
            figure = get_digit(array[j], i)
            dct[figure].append(array[j])
            j += 1
        for x in dct.values():
            lst += x
        array = lst.copy()
        lst.clear()
        dct = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        i += 1
        j = 0
    return array


# 1 helper

def get_digit(num, place):
    return floor(abs(num) / pow(10, place)) % 10


# 2 helper
def dt_cnt(fig):
    if fig == 0:
        return 1
    return floor(log10(abs(fig))) + 1


# 3 helper
def most_digits(nums):
    max_digit = 0
    i = 0
    while i < len(nums):
        max_digit = max(max_digit, dt_cnt(nums[i]))
        i += 1
    return max_digit


print(radix([1234, 56, 7, 32, 5453433, 432]))

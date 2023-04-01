# 1-1
from math import floor


def same(arr1, arr2):
    i = 0
    for x in arr1:
        if x * x not in arr2:
            i += 1
    if i > 0:
        return False
    return True


print(same([1, 4, 3], [16, 9, 1]))


# 1-2
def same_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    freq1 = {}
    freq2 = {}

    for x in arr1:
        if x not in freq1:
            freq1[x] = 1
        else:
            freq1[x] += 1

    for x in arr2:
        if x not in freq2:
            freq2[x] = 1
        else:
            freq2[x] += 1

    for x, y in freq1.items():
        if x * x not in freq2:
            return False

        if freq1[x] != freq2[x * x]:
            return False

    return True


print(same_arrays([1, 4, 3, 4], [16, 16, 9, 1]))


# 2-1
def valid_anagram(str1, str2):
    k_v = dict.fromkeys(str1 + str2, 0)
    for x in str1:
        k_v[x] += 1

    for x in str2:
        k_v[x] -= 1

    return not any(k_v.values())


print(valid_anagram('listen', 'silent'))


# 2-2
def another_anagram_example(str1, str2):
    if len(str1) != len(str2):
        return False

    look_up = {}
    i = 0

    while i < len(str1):
        let = str1[i]
        if let in look_up:
            look_up[let] += 1
            i += 1
        else:
            look_up[let] = 1
            i += 1

    i = 0
    while i < len(str2):
        let = str2[i]
        if let not in look_up or look_up[let] == 0:
            return False
        else:
            look_up[let] -= 1
            i += 1

    return True


print(another_anagram_example('listenn', 'silent'))


# 3-1
def mult_point(lst):
    right = len(lst) - 1
    left = 0
    while left < right:
        summ = lst[right] + lst[left]
        if summ == 0:
            return [lst[left], lst[right]]
        elif summ > 0:
            right -= 1
        else:
            left += 1


# 3-2-1
def count_unique(arr):
    new_list = []
    for x in arr:
        if x not in new_list:
            new_list.append(x)

    return len(new_list)


# 4-1
def max_seq(lst, num):
    sum_ = []
    temp_fig = []
    for x in lst:
        temp_fig.append(x)
        if len(temp_fig) == num:
            sum_.append(sum(temp_fig))
            temp_fig.pop(0)
    return max(sum_)


print(max_seq([4, 2, 1, 6, 2], 4))


# 4-2
def sum_seq(arr, num):
    maxSum = 0
    tempSum = 0

    if len(arr) < num:
        return None

    i = 0
    while i < num:
        maxSum += arr[i]
        i += 1

    tempSum = maxSum
    i = num
    while i < len(arr):
        tempSum = tempSum - arr[i - num] + arr[i]
        # actually [i - num] denotes sliding window =>
        # we move one index further every time and this
        # index represents 'past' value. It is subtracted from
        # temp figure and then we add new [i]
        maxSum = max(maxSum, tempSum)
        i += 1
    return maxSum


print(sum_seq([6, 9, 2, 1, 8, 5, 6, 3], 3))


# 5-2
def func_search(array, val):
    min_ = 0
    max_ = len(array) - 1

    while min_ < max_:
        middle = floor((min_ + max_) / 2)
        currentElement = array[middle]

        if currentElement < val:
            min_ = middle + 1

        elif currentElement > val:
            max_ = middle - 1

        else:
            return middle

    return -1


print(func_search([1, 3, 5, 6, 7, 9, 12, 16], 9))


# Exercises
# 1
def same_frequency(num1, num2):
    num1_ = str(num1)
    num2_ = str(num2)
    k_v = dict.fromkeys(num1_ + num2_, 0)

    for x in num1_:
        k_v[x] += 1

    for x in num2_:
        k_v[x] -= 1

    return not any(k_v.values())


print(same_frequency(182, 281))


# not partially mine
def sameFreq(num1, num2):
    num1 = str(num1)
    num2 = str(num2)

    if len(num1) != len(num2):
        return False

    countNum1 = dict()
    countNum2 = dict()

    for x in range(len(num1)):
        if num1[x] not in countNum1:
            countNum1[num1[x]] = 1
        else:
            countNum1[num1[x]] += 1

    for y in range(len(num1)):
        if num2[y] not in countNum2:
            countNum2[num2[y]] = 1
        else:
            countNum2[num2[y]] += 1

    for z in countNum1.keys():
        if len(countNum1.keys()) != len(countNum2.keys()):
            return False

        if z not in countNum2:
            return False

        elif countNum1[z] != countNum2[z]:
            print(countNum1[z], countNum2[z])
            return False

    return True


print(sameFreq(334, 344))


# 2
def are_dupl(*args):
    k_v = dict()
    for x in args:
        if type(x) != str:
            x = str(x)
        if x not in k_v:
            k_v[x] = 1
        elif x in k_v:
            k_v[x] += 1

    return any(x for x in k_v.values() if x > 1)


print(are_dupl(1, 2, 3))


# not mines (3)
def areDupl(*args):
    collection = dict()
    for x in args:
        if x not in collection:
            collection[args[x]] = 1
        else:
            collection[args[x]] += 1

    for x in collection:
        if collection[x] > 1:
            return True

    return False


def arePoint(*args):
    args = sorted(args)
    start_ = 0
    next_ = 1
    while next_ < len(args):
        if args[start_] == args[next_]:
            return True

        start_ += 1
        next_ += 1
    return False


print(arePoint('a', 't', 'g', 'a', 'p'))


def areShort(*args):
    return len(set(args)) != len(args)


print(areShort(1, 2, 3, 4))


# 3
def averPair(arr, fig):
    if len(arr) == 0:
        return False
    lst = list()
    i = 0
    while i < len(arr):
        lst.append(arr[i])
        if len(lst) == 2:
            if round((lst[0] + lst[1]) / 2) == fig:
                return True
            else:
                i += 1
                lst.pop(0)
        else:
            i += 1
    return False


print(averPair([1, 2, 3], 2.5))


def averPair(arr, fig):
    st = 0
    en = len(arr) - 1

    while st < en:
        avg = (arr[st] + arr[en]) / 2
        if avg == fig:
            return True
        elif avg > fig:
            en -= 1
        else:
            st += 1
    return False


# print(anotherPair([1, 2, 3], 2.5))


# 4
def isSubsequence(str1, str2):
    i = 0
    j = 0
    if not str1:
        return True
    while j < len(str2):
        if str2[j] == str1[i]:
            i += 1
        if i == len(str1):
            return True
        j += 1
    return False


print(isSubsequence('hello', 'hello world'))


# 'sing', 'sting'
# 'abc', 'abracadabra'
# 'abc', 'acb'


# 5
def maxSub(arr, num):
    if len(arr) < num:
        return False

    maxSub = 0
    tempSub = 0

    i = 0
    while i < num:
        maxSub += arr[i]
        i += 1

    tempSub = maxSub
    i = num

    while i < len(arr):
        tempSub = tempSub - arr[i - num] + arr[i]
        maxSub = max(tempSub, maxSub)
        i += 1
    return maxSub


print(maxSub([100, 200, 300, 400], 2))


# 6


# 7
def findLong(str_):
    score = 0
    total = 0
    var = ''
    for x in range(len(str_)):
        if str_[x] not in var:
            var += str_[x]
            score += 1
        else:
            score = 1
            var = str_[x]
        total = max(total, score)

    return total


print(findLong('thecatinthehat'))


# Colt's solution
def FindLong(str1):
    longest = 0
    seen = {}
    start = 0
    i = 0
    while i < len(str1):
        char = str1[i]
        if seen[char]:
            start = max(start, seen[char])
        longest = max(longest, i - start + 1)
        seen[char] = i + 1
        i += 1
    return longest


print(FindLong('thecatinthehat'))

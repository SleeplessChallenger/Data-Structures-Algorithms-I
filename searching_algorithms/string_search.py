# String search
# Naive one
def str_search(str1, str2):
    i = 0
    j = 0
    count = 0
    while i < len(str1):
        while j < len(str2):
            if str2[j] != str1[i + j]:
                i += 1
                j = 0
                break
            j += 1
            if j == len(str2) - 1:
                count += 1
    return count


print(str_search('wowomgzomg', 'omg'))

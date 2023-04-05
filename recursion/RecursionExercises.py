# First part
# 1
def power(num, exp):
    if exp == 0:
        """
        Base goes to the last condition (4 * power(4,0) -> which will be 1.
        Then: 1 * [4 * power(4,1)] which will be 4 => 1 * 4 and so on)
        """
        return 1

    return num * power(num, exp - 1)


print(power(4, 4))


def factor(x):
    if x < 0:
        return 0
    if x <= 1:
        return 1
    return x * factor(x - 1)


# 3
def product_of_array(arr):
    if len(arr) == 0:
        return 1

    total = arr[0]
    return total * product_of_array(arr[1:])


print(product_of_array([1, 4, 5, 7, 10]))


# 4
def recursive_range(num):
    if num == 0:
        return 0
    return num + recursive_range(num - 1)


print(recursive_range(5))


# 5
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Second part
# 1
def recur_str(expr):
    if len(expr) == 1:
        return expr[0]
    return expr[-1] + recur_str(expr[:-1])


print(recur_str('school'))


# 2
def is_palindrome(phr):
    if len(phr) == 1:
        return True
    # can be ok without 2 further lines
    if len(phr) == 2:
        return phr[0] == phr[1]

    if phr[0] == phr[-1]:
        return is_palindrome(phr[1:-1])
    return False


print(is_palindrome('WasItARatISaw'))


# not mine
def valid_palindrome(str1):
    if len(str1) == 1:
        return True
    if len(str1) == 2:
        return str1[0] == str1[1]
    if str1[0] == str1[-1]:
        return valid_palindrome(str1[1:-1])


# 3
# call_ = val = > val % 2 != 0


def check_call(arr, call_):
    if len(arr) == 0:
        return False

    if call_(arr[len(arr) - 1]):  # take last
        return True
    else:
        check_call(arr[:-1], call_)


# 4
def flatten(arr):
    if len(arr) == 0:
        return []
    if type(arr[0]) == int:
        return arr[:1] + flatten(arr[1:])
    return flatten(arr[0]) + flatten(arr[1:])


print(flatten([1, [2, [3, 4], [[5]]]]))


# 5
def cap_first(arr):
    new = []
    if len(arr) == 0:
        return []
    new.append(arr[0][0].upper() + arr[0][1:].lower())
    new += cap_first(arr[1:])
    return new


print(cap_first(['car', 'taco', 'banana']))


# 6
# here and in №9 we create new variable which is constantly changing => we implement +=
def nested_one(obj):
    sum_ = 0
    for x in obj:
        if type(obj[x]) == dict:
            sum_ += nested_one(obj[x])
        elif type(obj[x]) == int and obj[x] % 2 == 0:
            sum_ += obj[x]
    return sum_


print(nested_one(
    {'outer': 2, 'obj': {'inner': 2, 'otherObj': {'superInner': 2, 'notANumber': True, 'alsoNotANumber': "yup"}}}))


# 7
def capitalize_words(words):
    new = []
    if len(words) == 0:
        return []
    new.append(words[0].upper())
    new += capitalize_words(words[1:])
    return new


print(capitalize_words(['i', 'am', 'learning', 'recursion']))


# 8
# here we don't do any += stuff as we don't create anything new
def stringify(obj):
    for x in obj:
        if type(obj[x]) == dict:
            stringify(obj[x])
        elif type(obj[x]) == int:
            obj[x] = str(obj[x])
    return obj


print(stringify({'num': 1, 'test': [], 'data': {'val': 4, 'info': {'isRight': True, 'random': 66}}}))


# 9
def collect_strings(obj):
    arr = []
    for x in obj:
        if type(obj[x]) == str:
            arr.append(obj[x])
        elif type(obj[x]) == dict:
            arr += collect_strings(obj[x])
    return arr


print(collect_strings(
    {'stuff': "foo", 'data': {'val': {'thing': {'info': "bar", 'moreInfo': {'evenMoreInfo': {'weMadeIt': "baz"}}}}}}))


def collect_string(obj):
    arr = []

    def inner_string(dct):
        for x in dct:
            if type(dct[x]) == str:
                arr.append(dct[x])
            elif type(dct[x]) == dict:
                return inner_string(dct[x])

    inner_string(obj)
    return arr


print(collect_string(
    {'stuff': "foo", 'data': {'val': {'thing': {'info': "bar", 'moreInfo': {'evenMoreInfo': {'weMadeIt': "baz"}}}}}}))

"""
Accessing is O(1) as code doesn't go to every item and only access the one with the index
Adding/removing:
	* to the end is O(1)
	* at front O(n)
	* search O(n)

* O(log n) means how many times we need to multiply base to get n.
For ex, we have array with len = 32. So, log 32 = 5.
i.e. O(log n) decompositions

* O(n * log n). It means that despite array itself we have number of items
in the array that are to be compared every time.
For ex, we have array with 8 figures that we decompose till len(arr) == 1
So, on every circle we need to compare 8
i.e. O(n) comparisons per decomposition

* Radix sort
O(nk) in all Time complexity cases where k may be log n if all numbers are distinct
O(n+k) in all Space complexity cases
n = length of array
k - number of digits(average)

"""


def add_up(fig):
    total = 0
    while fig != 0:
        total += fig
        fig -= 1
    return total  # O(n)


print(add_up(6))


def add_up(fig):
    return int(fig * (fig + 1) / 2)  # O(1)


print(add_up(6))


def up_down(fig):
    fig2 = fig
    while fig != 0:  # these both loops have O(n)
        print(fig)
        fig -= 1
    while fig2 != fig:
        print(fig)
        fig += 1


print(up_down(10))


def nested_one(low, up):
    return [[x * y for x in range(low, up)] for y in range(low, up)]


print(nested_one(2, 5))


def double_loop(n):
    for x in range(1, n):  # Here O(n * n) => O(n^2). So, run time grows at the speed of n^2.
        for y in range(1, n):  # As the input 'n' grows how the output is reflected
            print(x * y)


double_loop(6)


def count_5(num):
    i = 0
    if num > 5:
        while i < num:
            i += 1
            yield i
    while i < 5:
        i += 1
        yield i


c = count_5(4)

for x in c:
    print(x)


def traverse_list_array():
    arr = [1, 2, 3, 4]
    lst = list()
    for i in arr:
        lst.append(arr[i])


def traverse_dict():
    k_v = {
        'name': 'Kelly',
        'isinstructor': True,
        'favonum': [1, 5, 8]
    }

    [x for x in k_v.keys()]  # O(n)

    if k_v.has_key('name'):  # O(1)
        print(f"k_v has name key")

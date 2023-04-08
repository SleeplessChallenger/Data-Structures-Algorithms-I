"""
Solving complex problems by breaking them down into a
collection of simpler sub-problems, solving each of those sub-problems just once,
and storing their solutions (aka remembering them)

We can use such an approach only in a particular case:
1)optimal substructure: problem has it if an optimal solution
can be constructed from optimal solutions of its
sub-problems
2)overlapping sub-problems: if problem can be broken down
into sub-problems which are reused several times
Ex: a) we take fib(5) and when we have fib(3) and fib(3) on both
ends there will be an equal fork after: fib(2) + fib(1) and the same on the
right b)take MergeSort. if we have same array [10,24,10,24].
When we split in half [10,24] and [10,24] => overlapping arrays
in other words: data that is evenly spaced across the array with repetition
then we can use dynamic programming
"""


def fib(x):
    if x <= 2:
        return 1
    return fib(x - 1) + fib(x - 2)


print(fib(5))

"""
In the realm of Big O the above written solution is horrendous
It's actually O(2^n) as the call stack grows immensely

Memoization
- Storing the results of expensive function calls and returning
- the cached result when the same inputs occur again

revamped solution
the n which subsequent results will end in base
is to be saved inside memo
Top-down approach
"""


def fib_new(n, memo=[]):
    if memo[n] is not None:
        return memo[n]
    if n <= 2:
        return 1
    res = fib_new(n - 1, memo) + fib_new(n - 2, memo)
    memo[n] = res
    return res


print(fib_new(5))


# Big O: O(N)

def fib_new_tweak(n, memo=[None, 1, 1]):
    if memo[n] is not None:
        return memo[n]
    res = fib_new_tweak(n - 1, memo) + fib_new_tweak(n - 2, memo)
    memo[n] = res
    return res


"""
Bottom-up approach
Storing the result of a previous result in a table (usually an array)
O(N), but won't hit stackoverflow error as recursive can
"""


def fib_tab(n):
    if n <= 2:
        return 1
    fib_nums = [0, 1, 1]
    i = 3
    while i <= n:
        fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]
        i += 1
    return fib_nums[i]

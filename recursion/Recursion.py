
"""
At first let's look at iterative
"""
import random


def take_shower():
    return "Showering!"


def eat_breakfast():
    meal = cook_food()
    return f"Eating {meal}"


def cook_food():
    items = ['Oatmeal', 'Eggs', 'Protein shake']
    return random.choice(items)


def wake_up():
    take_shower()
    eat_breakfast()
    print("OK, ready to go to work!")


wake_up()


# Baseline, Different input == recursive call

def count_down(num):
    # base case
    if num <= 0:
        print("All done!")
        return None

    print(num)
    num -= 1
    count_down(num)


count_down(5)


def sum_range(num):
    """
    here we have 'return' in the row below, hence the call stack after 1 is 'returned' will pop up
    one layer from call stack by one. While in the first recursion function we have only
    the 'return' in the base condition.
    """

    if num == 1:
        return 1
    return num + sum_range(num - 1)


sum_range(4)


def factorial(fig):
    total = 1
    i = fig
    while i > 1:
        total *= i
        i -= 1
    return total


factorial(5)


def recur_fact(fig):
    i = fig
    if i == 1:
        return 1
    return i * recur_fact(i - 1)


recur_fact(5)


# Helper method recursion
# 1
def collect_odd(arr):
    result = []

    def helper(helper_input):  # after in the helper base executed, we go to the outer function
        # and just return already appended array
        if len(helper_input) == 0:
            return

        if helper_input[0] % 2 != 0:
            result.append(helper_input[0])

        helper(helper_input.slice[1:])

    helper(arr)

    return result


collect_odd([1, 2, 3, 4, 5, 6, 7, 8, 9])


# resembles the one above, but with tweaks - Pure recursion method
def collect_nums(arr):
    """
    there is a sequence: new_arr on every recursive iteration call the function
    which also provides new 'new_arr' which will call and wait for the fucntion (same as above)
    to execute till the base case. And then in the backwards manner the function will
    construct the new_arr + the new_arr every time is blank that's why there will be
    either one number or blank array += function
    """
    new_arr = []

    if len(arr) == 0:
        return new_arr

    if arr[0] % 2 != 0:
        new_arr.append(arr[0])

    new_arr += (collect_nums(arr[1:]))
    return new_arr


print(collect_nums([1, 2, 3, 4, 5]))

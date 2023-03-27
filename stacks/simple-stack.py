"""
Stack is just a way of implementing the structure in such a way
that uses LIFO :last in first out
Generally, there are 2 variations: python(append and pop) & JS(push and pop) and
python(insert in the beginning and pop in the beginning) & JS(shift and unshift)

In our Stack Class we opted for shift and unshift() disguised
in push and pop. I.e. we'll add and remove from beginning 
rather than end as it is O(1) rather than O(n) in Singly Linked List
Because with append and pop we are to loop till the end
of the list. [!!!It's Singly Linked List]
"""


def simple_stack():
    # first variant with appending to the end
    stack = []

    stack.append(5)
    stack.append(8)
    stack.append(18)

    stack.pop()
    stack.pop()

    # second variant with appending to the start
    stack = []

    stack.insert(0, 5)
    stack.insert(0, 8)
    stack.insert(0, 18)

    stack.pop(0)
    stack.pop(0)


if __name__ == "__main__":
    simple_stack()

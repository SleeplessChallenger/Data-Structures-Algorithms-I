"""
Queue is also a way of just implementing particular structure.
Here FIFO is used: First in first out.

So as not to reindex the whole array it's much better to insert in the
beginning and remove from the end using
python(insert with index 0 and pop) & JS(unshift and pop) in array

But in Singly Linked List (another file in this repo) we've opted for adding
to the end and removing from the start.
"""


def simple_queue():
    # first variant with appending to the end
    q = []

    q.append('First')
    q.append('Second')
    q.append('Third')

    q.pop(0)
    q.pop(0)
    q.pop(0)

    # second variant with appending to the start
    q = []

    q.insert(0, 'First')
    q.insert(0, 'Second')
    q.insert(0, 'Third')

    q.pop()
    q.pop()
    q.pop()


if __name__ == "__main__":
    simple_queue()

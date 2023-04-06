"""
Big (O)
Insert O(1):
    *  hash the key
    * go to index in array
    * see key/values at that index in the array

    O(n) will be if hash function puts everything under one index

Deletion O(1)
Access O(1)
Searching: if key - O(1) and if value - O(n)

Good hash function should:
	* be fast
	* distribute keys uniformly
	* be deterministic (exact output every with certain input)
"""


# first version
def hash(key, array):
    total = 0
    for x in key:
        value = x.chr(0) - 96
        total = (total + value) % array
    return total


print(hash("pink", 10))


# Only hashes strings
# Not constant time - linear in key length
# Could be a little more random

# Slightly ameliorated

def hash_new(key, array):
    total = 0
    weird_prime = 31
    i = 0
    while i < min(len(key), 100):
        char = key[i]
        value = char.chr(0) - 96
        total = (total * weird_prime + value) % array
        i += 1
    return total


"""
To deal with collisions we can use: separate chaining & linear probing

First method involves 'at each index in array 
store values using more sophisticated data structure 
i.e. array (nested one) or linked list'

Second method: when collision is found we search through 
array to find the next empty slot, but it has limit of array length
"""

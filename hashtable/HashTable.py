"""
Look in hash_table_overview for overview
"""


class Hash:

    def __init__(self, size=54):
        self.keymap = []
        for x in range(size):
            self.keymap.append([])

    def hash_func(self, key):
        i = 0
        total = 0
        prime = 31
        while i < min(len(key), 100):
            x = key[i]
            val = ord(x) - 96
            total = (val * prime + total) % len(self.keymap)
            i += 1
        return total

    def set(self, key, value):
        index = self.hash_func(key)
        self.keymap[index].append([key, value])

    def get_value_by_key(self, key):
        """
        As in python I have list with blank [], I cannot simply
        check 'if self.keyMap[index]'. Thus, != is required
        """
        index = self.hash_func(key)
        if self.keymap[index]:
            for x in range(len(self.keymap[index])):
                if self.keymap[index][x][0] == key:
                    return self.keymap[index][x][1]
            else:
                return False
        return False

    def key(self):
        """
        traverse over hashtable and collect all keys
        """
        arr = list()
        for x in range(len(self.keymap)):
            # if list is empty we'll skip it
            if self.keymap[x]:
                for y in range(len(self.keymap[x])):
                    if self.keymap[x][y][0] not in arr:
                        arr.append(self.keymap[x][y][0])
        print(arr)
        return arr

    def value(self):
        """
        traverse over hashtable and collect all values
        """
        arr = list()
        for x in range(len(self.keymap)):
            if self.keymap[x]:
                for y in range(len(self.keymap[x])):
                    if self.keymap[x][y][1] not in arr:
                        arr.append(self.keymap[x][y][1])
        print(arr)
        return arr


"""
if we had empty array: self.keyMap = arr[size] like in JS
we could do the following:

def set(self,key,value):
 	node = self.hash_(key)
 	if not self.keyMap[node]:
 		self.keyMap[node] = []
 	self.keyMap[node].append([key,value])
"""

if __name__ == "__main__":
    hashy = Hash()

    hashy.set('Cool', 'Nice')
    hashy.set('Pink', 'Girl')
    hashy.set('Red', 'Ice_Cream')
    hashy.set('Brandish', 'Style')
    hashy.set('WowOmg', 'SuperbWatch')
    hashy.set('Interesting', 'Talk')
    hashy.set('Beautiful', 'Talk')
    hashy.set('Juicy', 'Talk')

    hashy.key()
    hashy.value()

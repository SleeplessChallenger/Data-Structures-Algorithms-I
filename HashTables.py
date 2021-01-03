#Big (O)
#Insert O(1)
#1)hash the key 2)go to index in array 3)see key/values at that index in the array
#O(n) will be if hash function puts everything under one index
#Deletion O(1)
#Access O(1)
#Searching: if key - O(1) and if value - O(n)

#Good hash function should: 1)be fast 2)distribute keys uniformly 3)be deterministic (exact output every
#with certain input)

#first version
def hash(key,array):
	total = 0
	for x in key:
		value = x.chr(0) - 96
		total = (total + value) % array
	return total

print(hash("pink",10))

#Only hashes strings
#Not constant time - linear in key length
#Could be a little more random

#Slightly ameliorated

def hash_new(key,array):
	total = 0
	weird_prime = 31
	i = 0
	while i < math.min(len(key),100):
		char = key[i]
		value = char.chr(0) - 96
		total = (total * weird_prime + value) % array
		i += 1
	return total


#To deal with collisions we can use: separate chaining & linear probing

#First method involves 'at each index in array 
#store values using more sophisiticated data structure 
#i.e. array (nested one) or linked list'

#Second method:when collision is found we search through 
#array to find the next empty slot, but it has limit of array length

import math

class Hash:

	def __init__(self,size = 54):
		self.keymap = []
		for x in range(size):
			self.keymap.append([])

	def hashFunc(self,key):
		i = 0
		total = 0
		prime = 31
		while i < min(len(key),100):
			x = key[i]
			val = ord(x) - 96
			total = (val * prime + total) % len(self.keymap)
			i += 1
		return total

	def set(self,key,value):
		index = self.hashFunc(key)
		self.keymap[index].append([key,value])


#As in python I have list with blank [], I cannot simply
#check 'if self.keyMap[index]'. Thus, != is required
	def get(self,key):
		index = self.hashFunc(key)
		if self.keymap[index] != []:
			for x in range(len(self.keymap[index])):
				if self.keymap[index][x][0] == key:
					return self.keymap[index][x][1]
			else:
				return False
		return False

	def key(self):
		arr = list()
		for x in range(len(self.keymap)):
			#if list is empty we'll skip it
			if self.keymap[x]:
				for y in range(len(self.keymap[x])):
					if self.keymap[x][y][0] not in arr:
						arr.append(self.keymap[x][y][0])
		print(arr)
		return arr

	def value(self):
		lst = list()
		for x in range(len(self.keymap)):
			if self.keymap[x]:
				for y in range(len(self.keymap[x])):
					if self.keymap[x][y][1] not in lst:
						lst.append(self.keymap[x][y][1])
		print(lst)
		return lst


	#if we had hollow array: self.keyMap = arr[size] like in JS
	#we could do the following:
	# def set(self,key,value):
	# 	node = self.hash_(key)
	# 	if not self.keyMap[node]:
	# 		self.keyMap[node] = []
	# 	self.keyMap[node].append([key,value]) 





hashy = Hash()

hashy.set('Cool','Nice')
hashy.set('Pink','Girl')
hashy.set('Red','Ice_Cream')
hashy.set('Brandish','Style')
hashy.set('WowOmg','SuperbWatch')
hashy.set('Interesting','Talk')
hashy.set('Beatiful','Talk')
hashy.set('Juicy','Talk')

hashy.key()
hashy.value()








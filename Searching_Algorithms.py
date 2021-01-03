#Linear search
def search(arr,val):
	for x in range(len(arr)):
		if arr[x] == val:
			return x
	return -1
print(search([2,5,1,6,9,10],5))

#second way
	for x in arr:
		if x == val:
			return arr.index(x)
	return -1


#Binary search
from math import floor
def bin_search(arr,phr):
	min_ = 0
	max_ = len(arr) - 1
	while min_ < max_:
		aver = floor((min_+max_)/2)
		if phr > arr[aver]:
			min_ = aver + 1
		elif phr < arr[aver]:
			max_ = aver - 1
		else:
			return phr
	return -1

	#slightly different, but doesn't work on my machine
	min_ = 0
	max_ = len(arr) - 1
	aver = floor((min_ + max_)/2)
	while arr[aver] != phr & min_ <= max_:
		if arr[aver] > phr:
			max_ = aver - 1
		else:
			min_ = aver + 1
	if arr[aver] == phr:
		return aver
	return -1


#String search
#Naive one
def str_search(str1,str2):
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

print(str_search('wowomgzomg','omg'))

#Bubble sort
#swap function
def swap(arr,idx1,idx2):
	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp

arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def bubble(arr):
	i = len(arr) - 1
	j = 0
	while i > 0:
		while i > j:
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				j += 1
			else:
				j += 1
		j = 0
		i -= 1
	return arr

print(bubble([2,14,6,23,1,10]))	 


def bubbleOptimized(arr):
	i = len(arr) - 1
	j = 0
	while i > 0:
		noSwap = True
		while j < i:
			if arr[j] > arr[j + 1]:
				arr[j],arr[j + 1] = arr[j + 1], arr[j]
				j += 1
				noSwap = False
			else:
				j += 1
		if noSwap:
			return arr
		i -= 1
		j = 0
	return arr
print(bubble([5,1,76,2,43,23,84,4,0,59,12]))


#reverse bubble
def bubble2(arr):
	i = 0
	j = len(arr) - 1
	noSw = True
	while i < len(arr):
		while j > i:
			if arr[j] > arr[j - 1]:
				arr[j - 1], arr[j] = arr[j], arr[j - 1]
				j -= 1
				noSw = False
			else:
				j -= 1
				noSw = True
		if noSw:
			return arr
		i += 1
		j = len(arr) - i


#Selection sort
def SelectionSort(arr):
	i = 0
	j = i + 1
	while i < len(arr):
		min_ = i
		while j < len(arr):
			if arr[min_] > arr[j]:
				min_ = j
				j += 1
			else:
				j += 1
		if min_ != i:
			arr[min_], arr[i] = arr[i], arr[min_]
		i += 1
		j = i + 1
	return arr
print(SelectionSort([5,1,76,2,43,23,84,4,0,59,12]))

#Reverse Selection
def Select2(arr):
	i = 0
	j = i + 1
	while i < len(arr):
		max_ = i
		while j < len(arr):
			if arr[j] > arr[max_]:
				max_ = j
				j += 1
			else:
				j += 1
		if max_ != i:
			arr[max_], arr[i] = arr[i], arr[max_]
		i += 1
		j = i + 1
	return arr
	

#InsertionSort
def InsertSort(arr):
	i = 1
	while i < len(arr):
		for x in range(len(arr[:i])):
			if arr[x] > arr[i]:
				arr[x], arr[i] = arr[i], arr[x]
		i += 1
	return arr


print(InsertSort([3,44,38,5,47,15]))



#not mine
def InSort(arr):
	i = 1
	j = i - 1
	while i < len(arr):
		min_ = arr[i]
		while j >= 0 and min_ < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1	#here wil be -1 when we swap 2 and 1
		arr[j + 1] = min_
		i += 1
		j = i - 1
	return arr
insertionSort([2,1,9,76,4])


#Merge sort
def merge(a,b):
	lst = list()
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if b[j] > a[i]:
			lst.append(a[i])
			i += 1
		else:
			lst.append(b[j])
			j += 1

	while i < len(a):
		lst.append(a[i])
		i += 1

	while j < len(b):
		lst.append(b[j])
		j += 1

	return lst

from math import floor, trunc
def sort(arr):
	if len(arr) == 1:
		return arr
	arr1 = sort(arr[:floor(len(arr)/2)])
	arr2 = sort(arr[trunc(len(arr)/2):])
	return merge(arr1, arr2)

print(sort([5,1,89,32,0,76,12]))


#Quick sort
def pivot(arr):
	count = 0
	i = 1
	piv = 0
	while i < len(arr):
		if arr[piv] > arr[i]:
			count += 1
			arr[i], arr[count] = arr[count], arr[i]
			i += 1
		else:
			i += 1
	arr[count],arr[piv] = arr[piv], arr[count]
	return count
print(pivot([26,23,27,44,17,47,39,42,43,1]))

#Quick sort
#same as above but with tweaks
def pivot(arr,st = 0,end = len(arr) + 1):
	i = st + 1
	count = 0
	piv = arr[st]
	while i < len(arr):
		if piv > arr[i]:
			count += 1
			arr[i], arr[count] = arr[count], arr[i]
			i += 1
		else:
			i += 1
	arr[count],arr[st] = arr[st], arr[count]
	return count

def quick(lng,left = 0,right = len(arr) - 1):
	if left < right:
		cnt = pivot(lng,left,right)
		quick(lng,left,cnt - 1)
		quick(lng,cnt + 1,right)
	return lng	
print(quick([26,23,27,44,17,47,39,42,43,1]))


#for python
def Qsort(arr):
	less = []
	equal = []
	great = []
	if len(arr) > 1:
		piv = arr[0]
		for x in arr:
			if piv > x:
				less.append(x)
			elif piv == x:
				equal.append(x)
			elif piv < x:
				great.append(x)
		return sort(less) + equal + sort(great)
	else:
		return arr
print(Qsort([26,23,27,44,17,47,39,42,43,1]))






#Radix sort
#1 helper
def getDig(num,place):
	num = str(num)[::-1]
	if place > len(num):
		return 0
	return int(num[place])

#2 helper
def digitCount(fig):
	fig = str(fig)
	return len(fig)
#print(fig(3238))

def max_num(arr):
	max_digit = 0
	i = 0
	while i < len(arr):
		max_digit = max(max_digit,length(arr[i]))
		i += 1
	return max_digit

#####from StackOverflow
#2 helper
from math import ceil, log10
def digitCnt(fg):
	if fg == 0:
		return 1
	return ceil(log10(abs(fg) + 1))
print(digitCnt(2741))
#####

#not mine
#1 helper
from math import floor, pow,log10
def gtDigit(num,place):
	return floor(abs(num)/pow(10,place)) % 10

#2 helper
def dtCnt(fig):
	if fig == 0:
		return 1
	return floor(log10(abs(fig))) + 1

#3 helper
def mostDigits(nums):
	maxDig = 0
	i = 0
	while i < len(nums):
		maxDig = max(maxDig,dtCnt(nums[i]))
		i += 1
	return maxDig

#fully mine
def radix(array):
	i = 0
	j = 0
	lst = list()
	dct = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
	max_dig = mostDigits(array)
	while i < max_dig:
		while j < len(array):
			figure = gtDigit(array[j],i)
			dct[figure].append(array[j])
			j += 1
		for x in dct.values():
			lst += x
		array = lst.copy()
		lst.clear()
		dct = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
		i += 1
		j = 0
	return array
print(radix([1234,56,7,32,5453433,432]))































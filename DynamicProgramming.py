#Solving comlplex problems by breaking them down into a 
#collection of simpler subproblems, solving each of those subproblems just once,
#and storing their solutions (aka remembering them)

#We can use such an approach only in a particular case:
#1)optimal substructure: problem has it if an optimal solution 
#can be constructed from optimal solutions of its
#subproblems
#2)overlapping subproblems: if problem can be broken down
#into subproblems which are reused several times
#Ex: a) we take fib(5) and when we have fib(3) and fib(3) on both
#ends there will be an equal fork after: fib(2) + fib(1) and the same on the
#right b)take MergeSort. if we have same array [10,24,10,24]. 
#When we split in half [10,24] and [10,24] => overlapping arrays
#in other words: data that is evenly spaced across the array with repetition 
#then we can use dynamic porgramming


def fib(x):
	if x <= 2:
		return 1
	return fib(x-1) + fib(x-2)
print(fib(5))


#in the realm of Big O the aforewritten aolution is horrendous
#It's actually O(2^n) as the call stack grows immensely

#Memoization
#Storing the results of expensive function calls and returning
#the cached result when the same inputs occur again

#revamped solution
#the n which subsequent results will end in base
#is to be saved inside memo
#Top-down approach
def fibNew(n, memo=[]):
	if memo[n] != None:
		return memo[n]
	if n <= 2:
		return 1
	res = fibNew(n-1,memo) + fibNew(n-2,memo)
	memo[n] = res
	return res
print(fibNew(5))

def fibNewtweak(n, memo=[None,1,1]):
	if memo[n] != None:
		return memo[n]
	res = fibNewtweak(n-1,memo) + fibNewtweak(n-2,memo)
	memo[n] = res
	return res

#Big O of the aforementioned: O(N)

#Bottom-up approach
#Storing the result of a previous result in a table (usually an array)
#O(N), but won't hit stackoverflow error as recursive can
def fibTab(n):
	if n <= 2:
		return 1
	fibNums = [0,1,1]
	i = 3
	while i <= n:
		fibNums[i] = fibNums[i-1] + fibNums[i-2]
		i += 1
	return fibNums[i]







import random

def take_shower():
    return "Showering!"

def eatBreakfast():
    meal = cookFood()
    return f"Eating {meal}"

def cookFood():
    items = ['Oatmeal', 'Eggs', 'Protein shake']
    return random.choice(items)

def wakeUP():
    take_shower()
    eatBreakfast()
    print("OK, ready to go to work!")
    
wakeUP()



#Baseline, Different input == recursive call

def countDown(num):
    if num <= 0:
        print("All done!")
        return-
    
    print(num)
    num -= 1
    countDown(num)

countDown(5)


def sumRange(num): #here we have 'return' in the row below, hence the call stack after 1 is 'retruned' will pop up 
                    #one layer from call stack by one. While in the first recursion fucntion we have only the 'return' in the
                    #base condition. 
                    
    if num == 1:
        return 1
    return num + sumRange(num - 1)
sumRange(4)


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


#Helper method recursion
#1
def outer(inp):
    outerScopeVar = []
    
    def helper(helperInp):
    	#modify the outerScopeVar
        helperInp -= helperInp
        helper(helperInp)
    
    helper(inp)
    
    return outerScopeVars

#2
def collectOdd(arr):
    result = []
    
    def helper(helperInput):		#after in the helper base executed, we go to the outer function
    								#and just return already appended array
        if len(helperInput) == 0:
            return 
    
        if helperInput[0] % 2 != 0:
            result.append(helperInput[0])
            
        helper(helperInput.slice[1:])
    
    helper(arr)
    
    return result

collectOdd([1,2,3,4,5,6,7,8,9])

#resembles the one above, but with tweaks - Pure recursion method

def alsoCollect(arr): #there is a sequence: newArr on every recursive iteration call the function
						#which also provides new 'newArr' which will call and wait for the fucntion (same as above)
						#to execute till the base case. And then in the backwards manner the function will 
						#construct the newArr + the newArr every time is blank that's why there will be
						#either one number or blank array += function
	newArr = []

	if len(arr) == 0:
		return newArr

	if arr[0] % 2 != 0:
		newArr.append(arr[0])

	newArr += (alsoCollect(arr[1:]))
	return newArr

print(alsoCollect([1,2,3,4,5]))
















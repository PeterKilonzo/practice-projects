#program to test what i have learned so far.
#the program asks the user for two values, evaluates the values according to some condition
#the function then performs some calculations on the user's values and displays them
#the code then appends the two values in a list and then prints the two values
def func(x,y):
    print(x+y)
    print(x*y)
    print(x%y)
    
x=int(input('enter the first value: '))
y=int(input('enter the second value: '))

if x>y:
    print('x is larger than y')
elif x==y:
    print('x is equal to y')
else:
    print('y is greater than x')


func(x,y)

import math
no1=math.sqrt(x)
no2=math.sqrt(y)

lst=[]
lst.append(x)
lst.append(y)


print(lst)

for x in lst:
    print(x, 'is your inputted value')

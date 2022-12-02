#program to practice conditional statements.
#the program gets values from the user, evaluates them and returns the results

a=int(input('enter the first number: '))
b=int(input('enter the second number: '))

if a>b:
    print(a, 'is greater than', b)
elif a<b:
    print(a, 'is smaller than', b)
else:
    print(a, 'is equal to', b)




grade=int(input('enter your grade: '))


if grade is in range(80,100):
    print('your grade is A')
elif grade is in range(70,89,1):
    print('your grade is B')
elif grade is in range(60,69,1):
    print('your grade is C')
elif grade is in range(50,59,1):
    print('your grade is D')
else:
    print('your grade is F')
    

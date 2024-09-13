#python program to find the factoriale of two numbers
def factorial(num):
    #one line two find the factorial
    return 1 if (num==1) or (num==0) else num * factorial(num-1)

#printing the values of nums 
num = 8
print("the factorial of num is" , factorial(num))

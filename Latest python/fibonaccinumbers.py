#python program to calculate tghe fibonacci numbers
def fibonacci(n):
    if n<=0:
        print("incoorect input")          #first fibonacci numbers is zero
    
    elif n==1:                  
        return 1                           #second fibonacci numbers is one 
    
    elif n==2:
        return 1  
    
    else:
        return fibonacci(n-1) +fibonacci(n-2)

#driver code
print(fibonacci(10))

    
    
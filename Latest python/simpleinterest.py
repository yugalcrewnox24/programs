#python program to find the simple interest 
def simpleinterest(p, t, r):
    print("the principle is" , p)
    print("the time is" , t)
    print("the rate is", r)

    si = p * t * r / 100
    print("the simple interest is",si)    
    return si

#driver code 
simpleinterest(2000, 1, 10)
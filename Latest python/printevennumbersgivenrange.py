#python program to find even numbers given range 
start = int(input("enter the start of range: "))
end = int(input("enter the end of range: "))

#iterating the each elements of list
for num in range(start, end+1):
    #cheacking the condition 
    if num%2 == 0:
     
     print(num, end = " ")

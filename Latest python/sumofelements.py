#python program to find the sum of elements of list
total = 0 
list1 = [2, 4, 5, 6, 8]
for elements in range(0, len(list1)):
    total = total + list1[elements]

#printing the result 
print("the total sum of list is: ", total)
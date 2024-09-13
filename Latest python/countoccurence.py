#python program to find the count occurence of elements
def countx(list1, x):
    count = 0  
    for ele in list1:
        if (ele == x):
           count = count + 1
        return count

list1 = [2, 4, 4, 4, 3, 8, 6]
x = 4
print('total occurence of elements in list'.format(x, countx(list1, x)))
        

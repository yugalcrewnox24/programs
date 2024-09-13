#python program to find the n largest elements in the list 
def nmaxelement(list1, n):
    final_list = []
    for i in range(0, n):
        max1 = 0
        for j in range(len(list1)):
            if list[j] > max1:
                max1 = list1[j]
                list1.remove(max1)
                final_list.append(max1)
    print(final_list)

#driver code 
list1 = [2, 6, 7, 8, 9, 5, 7, 10]
n = 2
#calling the function 
nmaxelement(list1, n)

#python program to copy the list for the original list
def cloning(list1):
    list2_copy = list1[:]
    return list2_copy

list1 = [24, 35, 46, 79, 78]
list2 = cloning(list1)
print("the original list is: ", list1)
print("the copying list is: ", list2)

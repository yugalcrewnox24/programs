#python program to remove elements in a given list
list1 = [3, 5, 8, 10, 12, 15]

for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)

#printing removing elements
print("after removing the even numbers in the list: ", list1)


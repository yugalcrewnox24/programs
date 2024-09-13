#python program to interchange first and last element 
def swaplist(newlist):
    size = len(newlist)
    #swapping
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp

newlist = [23, 45, 64, 21, 43, 41]
print(swaplist(newlist))
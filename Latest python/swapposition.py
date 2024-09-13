#python program to swap an position of an givenlist
def swappositon(list, pos1, pos2):
    list[pos1] , list[pos2] = list[pos2] , list[pos1]
    return list

#driver code 
list = [34, 43, 54, 65, 67]
pos1 ,pos2 = 1, 3
print(swappositon(list, pos1, pos2))

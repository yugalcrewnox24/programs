#python program to calculate the reverse array of number
def rversarray(arr, d):
    c = (arr[d: ]) + (arr[: d])
    return c
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
print(rversarray(arr, d))



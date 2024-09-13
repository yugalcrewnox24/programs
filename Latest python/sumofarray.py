#python program to calcuate the sum of array 
def _sum(array):
    sum  = 0
    for i in array:
        sum = sum + i
    return(sum)

if __name__ == "__main__":
    array = [12, 3, 4, 6, 7]
    n = len(array)
    ans = _sum(array)
    print("the sum of array is: ", ans)


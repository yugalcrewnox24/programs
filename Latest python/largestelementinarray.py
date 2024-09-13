#python program to calculate the largest element in the array 
def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


#driver code 
arr = [64, 78, 56, 46, 456]
n = len(arr)
ans = largest(arr, n)

print("thr largest number is: ", ans)

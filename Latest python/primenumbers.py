#python program to print the prime numbers for an guven intervel
def num(x, y):
    prime_list = []
    for i in range(x, y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
                else:
                    prime_list.append()
    return prime_list
#driver code 
starting_point = 2
ending_point = 7
lst = (starting_point, ending_point)
if len(lst)==0:
    print("there is no prime numbers in this list")

else:
    print("the prime numbers in this range is: ", lst)


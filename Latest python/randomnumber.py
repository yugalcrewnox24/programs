#python program to select an random numbers from an list 

import random

test_list = [4, 6, 75, 7, 8]

#print the original list
print("the original list: " + str(test_list))

#used random.choice() to get an numbers 
random_num = random.choice(test_list)

#print the random number
print("the selected random number: " + str(test_list))



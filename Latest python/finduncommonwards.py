#python progam to find the uncommon wards form the string 

def uncommonword(a, b):

    #count ward contain all count wards 
    count = 0
    for word in a.split():
        count[word] = count.get(word, 0) + 1
    
    for word in b.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] = 1]

#driver code 
a = ["geeks for geeks"]
b = ["geeks for geeks is best platform "]

#printing the ans
print("the uncommon word is: ", uncommonword(a, b))



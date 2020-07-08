# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def unique(n):    
    result = ""
    list_set = set(n) 
    unique_list = (list(list_set)) 
    for x in unique_list: 
        result = result + str(x)
    return result
    
lijst = []
setje = set()

for i in range(2000):
    for j in range(2000):
        lijst.clear()
        r = i*j
        n = str(r) + str(i) + str(j)
        if len(n) == 9:
            for item in n:
                lijst.append(item)
            x = unique(lijst)
            if len(x) == 9:            
                if "0" not in x:
                    print("Som is: i",i,"  j ",j,"  r ",r)  
                    setje.add(int(r))

print("Totaal: ", sum((setje)))
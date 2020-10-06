# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.


import sys

cubes = list()
probeersel = list()

for i in range(1 ,8501):
    result = (i**3)
    b = "".join(sorted(str(result)))
    cubes.append(b)
    probeersel.append(str(b) + " " + str(result))
    if i % 8500  == 0:
        for element in cubes:
            if cubes.count(element) == 5:
                print("Result is: ", element)
                for i in probeersel:
                    if (str(element) in i):
                        print(i)
                        sys.exit()

# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

from itertools import permutations

cubes = set()

def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        cubes.add(n)
    else:
        return False

def permutated_numbers(y):
    return [''.join(i) for i in permutations(y)]

for i in range(100000000,1000000000):
    is_cube(i)

print(cubes)
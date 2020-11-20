# Many numbers can be expressed as the sum of a square and a cube. Some of them in more than one way.
# Consider the palindromic numbers that can be expressed as the sum of a square and a cube, both greater than 1, in exactly 4 different ways.
# For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:
# 22852 + 203
# 22232 + 663
# 18102 + 1253
# 11972 + 1563
# Find the sum of the five smallest such palindromic numbers.

# gebruteforced... mag wel betahh

import sys

squares = []
cubes = []
for i in range(1,50000):
    squares.append(i**2)
    cubes.append(i**3)

print('Squares and Cubes generated')

count = 0
res = []
for square in squares:
    count+=1
    if count % 1000 == 0:
        print('---------------Tussenstantje: ', count)
    for cube in cubes:
        n = square+cube
        if n > 5000000:
            if n < 1100000000:
                if int(str(n)[::-1]) == n:
                    res.append(n)
                    if len((sorted(set([i for i in res if res.count(i)==4])))) == 5:
                        print('Result: ', sum(sorted(set([i for i in res if res.count(i)==4]))))
                        sys.exit()
            else:
                break
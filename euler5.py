#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
i = 200000000
loop = True

while loop:
    i += 2
    if i % 10000000 == 0:
        print('tussenstand ', i)
    if all(i % j == 0 for j in divisors):
        print("Result: ", i)
        loop = False
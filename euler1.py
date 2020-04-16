#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

numberList = list(range(999 + 1))
result = 0

for x in numberList:
    if (x % 3 == 0) or (x % 5 == 0):
        result = result + x
print(result)

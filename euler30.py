# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

numbersResult = []
for items in range(2,999999):
    digits = [int(x) for x in str(items)]
    a = 0
    b = 0
    count = 0
    for i in digits:
        a = i**5
        b = b + a
        count = count + 1
        if count == len(str(items))  and b == items:
            print("Succes! ", b, "    Digits: ", items)
            numbersResult.append(b)

print("Sum of the numbers: ", sum(numbersResult))
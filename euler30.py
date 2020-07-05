# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# x = 1**4 + 6**4 + 3**4 + 4**4
# y = 8**4 + 2**4 + 0**4 + 8**4
# z = 9**4 + 4**4 + 7**4 + 4**4
# print(x)
# print(y)
# print(z)

numbers = []
for i in range (10000,100000):
    numbers.append(i)

result = 0
superResult = set()
dinges = []
for i in range(0,10):
    result = 0
    macht = i**5
    dinges.append(macht)
    for j in range(0,10):
        for k in range(0,10):
            try:
                result = dinges[j] + dinges[k] + dinges[k+1] + dinges[k+2] + dinges[k+3]
            except:
                print("Exception")
            if result in numbers:
                superResult.add(result)

for items in superResult:
    digits = [int(x) for x in str(items)]
    a=0
    b=0
    for i in digits:
        a = i**5
        b = b + a
        print(b)
        if b in superResult:
            print("Succes! ", b)

print(superResult)

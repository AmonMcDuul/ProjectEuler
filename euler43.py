# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations 

number = '0123456789'
superResult = 0

for i in permutations(number):
    count = 0
    workingNumber = i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + i[9]
    sum1 = i[1] + i[2] + i[3]
    sum2 = i[2] + i[3] + i[4]
    sum3 = i[3] + i[4] + i[5]
    sum4 = i[4] + i[5] + i[6]
    sum5 = i[5] + i[6] + i[7]
    sum6 = i[6] + i[7] + i[8]
    sum7 = i[7] + i[8] + i[9]
    if int(sum1) % 2 == 0 and int(sum2) % 3 == 0 and int(sum3) % 5 == 0 and int(sum4) % 7 == 0 and int(sum5) % 11 == 0 and int(sum6) % 13 == 0 and int(sum7) % 17 == 0:
        superResult += int(workingNumber)
        print("we have got one: ", workingNumber)
print(superResult)
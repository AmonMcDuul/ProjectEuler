# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
# For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
# Leading zeroes are not allowed in either n or reverse(n).
# There are 120 reversible numbers below one-thousand.
# How many reversible numbers are there below one-billion (109)?

count = 0
for i in range(11,10**9,2):
    if i % 1000001 == 0:
        print('Tussenstandje: ', i)
    x = int(str(i)[0])
    if x % 2 == 0:
        r = i + int(str(i)[::-1])
        c = 0
        for num in str(r):
            if int(num) % 2 != 0:
                c += 1
            if int(num) % 2 == 0:
                break
        if c == len(str(r)):
            count +=1

print(count*2)
# How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?

from itertools import combinations_with_replacement
l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,0,0,0]

combinations = combinations(l,18)

length = sum(1 for x in combinations)
print(length)

result = 0
for i in combinations:
    if result % 100000000 == 0:
        print(result, ' Tussenstandje')
    result+=1

print(result*0.9)

# 227485267000992000
# 6402373705728000
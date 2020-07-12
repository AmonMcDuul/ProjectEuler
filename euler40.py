# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

number = []
for i in range(1,1000001):
    for item in str(i):
        number.append(int(item))
result = (number[0]*number[9]*number[99]*number[999]*number[9999]*number[99999]*number[999999])
print(result)
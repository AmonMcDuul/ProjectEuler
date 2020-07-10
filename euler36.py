# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# n = bin(585)[2:].zfill(8)
# print(n)

def palindrome(n):
    return str(n) == str(n)[::-1]

result = 0
for i in range(1000000):
    n = bin(i)[2:].zfill(8)
    if palindrome(int(n)) and palindrome(i):
        # print("Succes!",n," <n - i> ",i)
        result += i

print(result)
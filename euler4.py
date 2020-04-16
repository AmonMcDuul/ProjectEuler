#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

lijst = list(range(100, 1000))
lijst.reverse()
product = 0
result = 0

for i in lijst:
    for j in lijst:
        product = i * j
        if(str(product) == str(product)[::-1]) and (result < product):
            result = product
print(result)
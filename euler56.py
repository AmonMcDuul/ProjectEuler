# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

biggestSum = 0
for i in range(1,100):
    for j in range(1,100):
        digitalSum = 0
        r = i**j
        for n in (str(r)):
            digitalSum+=int(n)
        if biggestSum < digitalSum:
            biggestSum = digitalSum

print(biggestSum)
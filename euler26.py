def repeatingNumbers(a, b):
    n = a % b
    if n == 0:
        return 0

    decimals = {}
    n = n * 10
    position = 0

    while True:
        position += 1
        n = n % b
        if n in decimals:
            i = decimals[n]
            return position - i
        else:
            decimals[n] = position
        n = n * 10

results = 0
highest = 0
for i in range(2,1000):
    if (repeatingNumbers(1,i) > results):
        results = (repeatingNumbers(1,i))
        highest = i
print(highest)
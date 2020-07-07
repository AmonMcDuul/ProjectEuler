numbersResult = []

for items in range(1000,9999):
    digits = [int(x) for x in str(items)]
    a=0
    b=0
    count=0
    for i in digits:
        a = i**4
        b = b + a
        count = count + 1
        if count == 4 and b == items:
            print("Succes! ", b, "    Digits: ", items)
            numbersResult.append(b)

print(sum(numbersResult))

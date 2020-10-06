# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

count = 0
for num in range(1,100):
    for pows in range(1,100):
        result = num ** pows
        if len(str(result)) == pows:
            # print(result, "length: ", len(str(result)), "powers: ", num, "**", pows )
            count +=1
print(count)
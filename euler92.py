# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

count = 0
for i in range(1,10000000):
    if i % 10000 == 0:
        print('Tussenstandje: ', i)
    control = i
    s = set()
    s.clear()
    loop = True
    while loop:
        if i == 89:
            count +=1
            loop = False
        if i == 1:
            loop = False
        i = str(i).replace('0', '')
        l = len(str(i))
        c = 0
        n = 0
        for j in str(i):
            if int(j) is not 0:
                r = int(j)**2
                n += r
                c += 1
                i = n
                if c == l:
                    if n not in s:
                        s.add(n)
                    else:
                        loop = False
print(count)

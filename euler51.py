# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
#  yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

def sieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    primeList = []
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]: 
           primeList.append(p)
    return primeList

numbers = set(sieveOfEratosthenes(1000000))

firstPrime = 0
result = 1000000
for primes in numbers:
    acount=0
    bcount=0
    ccount=0
    dcount=0
    ecount=0
    fcount=0
    gcount=0
    hcount=0
    jcount=0
    kcount=0

    aa = 0
    bb = 0
    cc = 0
    dd = 0
    ee = 0
    ff = 0
    gg = 0
    hh = 0
    jj = 0
    kk = 0

    if len(str(primes)) == 6:
        for i in range(0,10):
            # xXxXxX
            a = str(i) + str(primes)[1:2] + str(i) + str(primes)[3:4] + str(i) + str(primes)[5:6]
            # xXxxXX 
            b = str(i) + str(primes)[1:2] + str(i) + str(i) + str(primes)[4:6] 
            # xXXxxX 
            c = str(i) + str(primes)[1:3] + str(i) + str(i) + str(primes)[5:6] 
            # xxXxXX 
            d = str(i) +str(i) + str(primes)[2:3] + str(i) + str(primes)[4:6] 
            # xxXXxX
            e = str(i) +str(i) + str(primes)[2:4] + str(i) + str(primes)[5:6]  
            # xxxXXX 
            f = str(i) +str(i) + str(i) + str(primes)[3:6]
            # XxxxXX 
            g = str(primes)[0:1] + str(i) +str(i) + str(i) + str(primes)[4:6]
            # XxxXxX 
            h = str(primes)[0:1] + str(i) + str(i) + str(primes)[3:4] + str(i) + str(primes)[5:6] 
            # XxXxxX 
            j = str(primes)[0:1] + str(i) + str(primes)[2:3] + str(i) + str(i) + str(primes)[5:6] 
            # XXxxxX 
            k = str(primes)[0:2] + str(i) + str(i) + str(i) + str(primes)[5:6]
            
            zero = a.startswith('0')
            if zero == False:
                if int(a) in numbers:
                    acount+=1
                if int(b) in numbers:
                    bcount+=1
                if int(c) in numbers:
                    ccount+=1
                if int(d) in numbers:
                    dcount+=1
                if int(e) in numbers:
                    ecount+=1
                if int(f) in numbers:
                    fcount+=1
            if int(g) in numbers:
                gcount+=1
            if int(h) in numbers:
                hcount+=1
            if int(j) in numbers:
                jcount+=1
            if int(k) in numbers:
                kcount+=1

            if acount == 1:
                aa = a
            if bcount == 1:
                bb = b
            if ccount == 1:
                cc = c
            if dcount == 1:
                dd = d
            if ecount == 1:
                ee = e
            if fcount == 1:
                ff = f
            if gcount == 1:
                gg = g
            if hcount == 1:
                hh = h
            if jcount == 1:
                jj = j
            if kcount == 1:
                kk = k

            if acount > 7:
                if primes < result:
                    result = primes
                    firstPrime = aa
            if bcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = bb
            if ccount > 7:
                if primes < result:
                    result = primes
                    firstPrime = cc
            if dcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = dd
            if ecount > 7:
                if primes < result:
                    result = primes
                    firstPrime = ee
            if fcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = ff
            if gcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = gg
            if hcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = hh
            if jcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = jj
            if kcount > 7:
                if primes < result:
                    result = primes
                    firstPrime = kk
print(result, " FirstPrime: ", firstPrime)
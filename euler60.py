# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# 3673 6733 7673 6737 109673 673109

import sys

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

numbers = sieveOfEratosthenes(100000)
numberslargeList = sieveOfEratosthenes(100000000)
numberLarge = set(numberslargeList)

superResult = 10000000

for i in range(0,1220):
    priemEen = numbers[i]
    for j in range(i,1220):
        priemTwee = numbers[j]
        a = str(priemEen) + str(priemTwee)
        b = str(priemTwee) + str(priemEen)
        if int(a) in numberLarge and int(b) in numberLarge:
            for k in range(j,1220):               
                priemDrie = numbers[k]
                a = str(priemEen) + str(priemDrie)
                b = str(priemDrie) + str(priemEen)
                c = str(priemTwee) + str(priemDrie)
                d = str(priemDrie) + str(priemTwee)
                if int(a) in numberLarge and int(b) in numberLarge:
                    if int(c) in numberLarge and int(d) in numberLarge:
                        for l in range(k,1220):
                            priemVier = numbers[l]
                            a = str(priemEen) + str(priemVier)
                            b = str(priemVier) + str(priemEen)
                            c = str(priemTwee) + str(priemVier)
                            d = str(priemVier) + str(priemTwee)
                            e = str(priemDrie) + str(priemVier)
                            f = str(priemVier) + str(priemDrie)
                            if int(a) in numberLarge and int(b) in numberLarge:
                                if int(c) in numberLarge and int(d) in numberLarge:
                                    if int(e) in numberLarge and int(f) in numberLarge:
                                        for m in range(l,1220):
                                            priemVijf = numbers[m]
                                            a = str(priemEen) + str(priemVijf)
                                            b = str(priemVijf) + str(priemEen)
                                            c = str(priemTwee) + str(priemVijf)
                                            d = str(priemVijf) + str(priemTwee)
                                            e = str(priemDrie) + str(priemVijf)
                                            f = str(priemVijf) + str(priemDrie)
                                            g = str(priemVier) + str(priemVijf)
                                            h = str(priemVijf) + str(priemVier)
                                            if int(a) in numberLarge and int(b) in numberLarge:
                                                if int(c) in numberLarge and int(d) in numberLarge:
                                                    if int(e) in numberLarge and int(f) in numberLarge:
                                                        if int(g) in numberLarge and int(h) in numberLarge:
                                                            if priemVier != priemVijf:
                                                                print("resultaat: ", priemEen, priemTwee, priemDrie, priemVier, priemVijf)
                                                                x = priemEen + priemTwee + priemDrie + priemVier + priemVijf
                                                                print("sum: ", x)
                                                                if x < superResult:
                                                                    superResult = x
                                                                    print("    kleinste result tot nu toe: ", superResult, " with numebrs: ", priemEen, priemTwee, priemDrie, priemVier, priemVijf)
print("Result: ", superResult)
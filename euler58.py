
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

numbers = set(sieveOfEratosthenes(1000000))

for i in range(5000,5001):
    lastNumber = i*i
    numbers = []
    elem = 0
    result = 1
    count=0
    primes = set()
    begin = 4
    skip = 0
    size = 3
    minus = 0

    for item in range(1,lastNumber+1,2):
        numbers.append(item)
    for btem in range(1,lastNumber):
        if btem in numbers:
            primes.add(btem)
    for times in range(1,1000000,1):
        if times % 100 == 0:
            print(times, minus, result+1)
        try: 
            if count > 3:
                skip += 1
                count = 0
                size +=1
            if count <= begin:
                elem += skip
                minus +=1
                if numbers[times+elem] in primes:
                    result+=1 
                    minus+=1
                    # print(numbers[times+elem])
            count+=1
            if result*10 < minus:
                print("Dit issemmm", i)
                sys.exit()
        except:
            break
    # print(len(primes), result+1)
    print (result +1, '<result minus>  ', minus, "   i:" , i)
        
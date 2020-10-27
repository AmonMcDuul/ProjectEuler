# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

from math import ceil, sqrt
from collections import Counter

def EratosthenesSieve(N:int)-> list:
    '''
    Calculating SPF (Smallest Prime Factor)
    for every number till N.
    Time Complexity : O(NloglogN)
    '''
    N+=1
    # stores smallest prime factor for every number
    spf = [*range(N)]
    
    # separately marking spf for every even number as 2 
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, ceil(sqrt(N))): 
        # checking if i is prime
        if (spf[i] == i):
            # marking SPF for all numbers divisible by i
            for j in range(i * i, N, i):
                # marking spf[j] if it is not previously marked 
                if (spf[j] == j):
                    spf[j] = i
    return spf


def getReducedFactorization(N:int, spf:list)-> int:
    """
    counts repetition of each prime from prime factorisation of N
    using trial method upon spf list, and calculating the ceil of 
    half of all prime's powers (pow(p, ceil(a/2))) and multiplying 
    them together.
    """
    gamma = 1
    while (N!=1):
        # keep a prime in prev variable
        prev=spf[N]
        # for counting the power
        c=0
        # counts power of a prime
        while spf[N]==prev:
            c+=1
            N//=spf[N]
        # multiplies the half ceil of power on primes
        gamma*=pow(prev, ceil(c/2))
        prev=spf[N]
    return gamma


def pythagoreanTriplets(n):
    # calculate spf array
    spf=EratosthenesSieve((n - int(sqrt((n<<1) -1)))<<1)
    # keeps the triplet count
    tripletCount=0
    # loopinf for every values of 2*b
    for b2 in range(4, (n - int(sqrt((n<<1) -1)))<<1, 2):
        # calculates reduced factor of 2*b
        gamma=getReducedFactorization(b2, spf)
        
        # for findin all triplets from 2*b
        for i in range(1, int(sqrt(b2*((b2>>1)-1)))//gamma+1):
            i*=gamma
            sqVal = i*i
            q=sqVal//b2
            # if z = q+i+(b2>>1) > n break else print triplet
            if q+i+(b2>>1)>n:
                break
            else:
                # remove comments in this else block to print Triplets
                x=q+i
                if x + (b2>>1)+i + x+(b2>>1) < 1500000:
                    l.append(x + (b2>>1)+i + x+(b2>>1))
                # tripletCount+=1
    return tripletCount

l = []
n=1500000
pythagoreanTriplets(n)
a = dict(Counter(l))
print(Counter(a.values())[1])
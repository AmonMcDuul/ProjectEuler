# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

def pythagoras(a,b,c):
    if a**2 + b**2 == c **2:
        return True
    return False

result = 0

for p in range(1,1000):
    count = 0
    k=0
    if p % 100 == 0:
        print(p)
    for i in range (1,p):
        for j in range(1,p):
            k = p-i-j
            if k < 0:
                break
            r = i+j+k
            if  r == p:
                if pythagoras(i,j,k):
                    count +=1
                    if count > result:
                        result = count
                        print("new winner is:" ,p ," with these counts: " ,result/2)
            if r > p:
                break

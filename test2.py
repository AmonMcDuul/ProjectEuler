number = 1504170715041707
mini = 1504170715041708
modi = 4503599627370517

def Solve():
    global mini
    for n in range(1,pow(2,30)):
        N=(number*n)%modi
        if N<mini:
            mini=N
            print("Index number=",n,"coin=",mini)          
Solve()
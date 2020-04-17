#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

number = 100

def factoralDigitSum(n):
    result = n
    for i in range(n,1,-1):
        result *= (i-1)
    return(result) 

print (sum(map(int, str(factoralDigitSum(number)))))
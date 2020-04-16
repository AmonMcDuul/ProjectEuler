#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number=600851475143
i=1
result=1

while(i <= number):
    prime=0
    if(number % i == 0):
        j=1
        while(j <= i):
            if(i % j == 0):
                prime=prime+1
            j=j+1
        if(prime == 2):
            result = result * i
            if(result == number):
                print("Largest prime factor: ", i)
                break
    i=i+1
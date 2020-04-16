#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#=  brute force.. moet nog aangepast worden

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]
inputList = list(range(20000000, 250000000))
print(primeNumbers)
for i in inputList:
    if all(i % j == 0 for j in primeNumbers):
        print("cool: ", i)
        exit() 
#The sum of the squares of the first ten natural numbers is,
#2+22+...+102=385
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)2=552=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


lijst = list(range(1, 101))
squareOfSum = 0

sumOfSquare = sum(i*i for i in lijst)

for i in lijst:
    squareOfSum = (squareOfSum + i)
squareOfSum = squareOfSum * squareOfSum

result = squareOfSum - sumOfSquare
print("squareOfSum: ", squareOfSum, " - ", "sumOfSquare", sumOfSquare," = ", "Resultaat: ", result)
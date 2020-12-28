# 70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
# What is the expected number of distinct colours in 20 randomly picked balls?
# Give your answer with nine digits after the decimal point (a.bcdefghij).

from math import factorial

print(7 * (1 - (factorial(60) / (factorial(20) * factorial(60 - 20))) / (factorial(70) / (factorial(20) * factorial(70 - 20)))))
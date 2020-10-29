# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
# However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
# NOTE: The first two lines in the file represent the numbers in the example given above.

import numpy
import math

c=[]
result = 0
count = 0
line = 0
for item in open("euler99numbers.txt"):
    line +=1
    values = [int(x) for x in [item.strip()][0].split(',') if x]
    a = values[0]
    b = values[1]
    x = b * math.log(a, 10)
    if x > count:
        count = x
        result = line     
print("Result: ", result)
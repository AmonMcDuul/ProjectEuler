# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction

result = 1
setjebetje = set()
stringetje = ""
dubbel = []

for i in range(10,100):
    for j in range(i+1,100):
        stringetje = str(i)+str(j)
        for item in stringetje:
            if item in setjebetje:
                dubbel.append(item)
            setjebetje.add(item)      
        if len(setjebetje) == 3:
            if '0' not in setjebetje:
                if len(dubbel) != 0:
                    num = list(str(i))
                    den = list(str(j))
                    for items in num:
                        if dubbel[0] in num:
                            num.remove(dubbel[0])
                    for btems in den:
                        if dubbel[0] in den:
                            den.remove(dubbel[0])                    
                    if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):
                        print(i,"/",j)
                        result *= Fraction(i,j)

        dubbel.clear()            
        setjebetje.clear()
print(result)
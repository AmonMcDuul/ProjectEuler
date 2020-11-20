def euler171() :
	#s = "987654321"
	s=[9,8,7,6,5,4,3,2,1]
	top = 81*5
	t = int(0.5 + top ** 0.5)
	squares = [x * x for x in range(1, t) if x*x <= top ] 
	for sq in squares :
		x = [y for y in compose(s, 0, 0, sq)]
		for xx in x :
			if test(xx, sq) :
				ss = "".join(str(c) for c in xx)
				print (ss)

euler171()

import math

t = 0
for x in range(1, 51):
    for y in range(1, 50):
        m = math.gcd(x, y)
        t += min(x*m//y, m*(50-y)//x)
print (t)
print(50*50*3)
print ('Result = ', t*2 + 50*50*3)
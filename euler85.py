# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

def rectCount(n, m):
    return (m * n * (n + 1) * (m + 1)) // 4

for i in range(1,1000):
    for j in range(i,1000):
        if 1999900 < rectCount(i, j) < 2000100:
            print(rectCount(i,j), i, j, '    ', i*j)
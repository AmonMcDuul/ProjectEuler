# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
# by only moving to the right and down, is indicated in bold red and is equal to 2427.
# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt 
# (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

matrix = []
with open('euler81matrix.txt') as f:
    for line in f:
        matrix.append([int(n) for n in line.strip('\n').split(',')])

def minimalPathSum(n):
    result = n
    for i in reversed(range(len(n))):
        for j in reversed(range(len(n[i]))):
            if i + 1 < len(n) and j + 1 < len(n[i]):
                number = min(n[i + 1][j], n[i][j + 1])
            elif i + 1 < len(n):
                number = n[i + 1][j]
            elif j + 1 < len(n[i]):
                number = n[i][j + 1]
            else:
                number = 0
            result[i][j] += number
    return result[0][0]

print(minimalPathSum(matrix))

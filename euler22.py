#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?

#functie maken om letters en waarde te checken

def alphabetNumber(n):
    alphabet =  ["", "A","B","C","D","E", \
        "F","G","H","I", "J", \
            "K", "L", "M", "N", \
            "O", "P", "Q", "R", \
            "S", "T", "U","V", "W",\
            "X", "Y", "Z"]
    return (alphabet.index(n))

f = open("C:/Users/Joran/Desktop/p022_names.txt")
names = f.read()
names = names.replace('"', "")
names = names.split(",")
names.sort()

result = 0
for i in names:
    index = 0
    y = 0
    for j in i:
        x = alphabetNumber(j)
        y += x
    index = names.index(i) +1
    result += (y * index)
print (result)
f.close()
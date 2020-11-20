# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. 
# What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. 
# We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted,
#  neither may a different letter have the same digital value as another letter.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
#  find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
# What is the largest square number formed by any member of such a pair?
# NOTE: All anagrams formed must be contained in the given text file.

squares = []
for i in range(1, 50000):
    squares.append(i**2)
# print(squares)

def annagram_square(square, word_one, word_two):
    l = {}
    for i in range(len(word_one)):
        l[word_one[i]] = str(square)[i]
    result = ""
    for i in word_two:
        result += l[i]
    return int(result)

def is_square(n):
    return (n**0.5) % 1. == 0

my_file = open("euler98numbers.txt", "r")
content = my_file.read()
content_list = content.split(",")

l = {}
temp = []
for i in content_list:
    l[i]=sorted(i)
    temp.append(sorted(i))

words = []
for i in l:
    count = 0
    for j in temp:
        if l.get(i) == j:
            count += 1
            if count == 2:
                words.append(i)

square_set = set()
word_set = set()

result = 0
count = 0
for i in words:
    count +=1  
    word_set.clear()
    for c in i:
        word_set.add(c)
    for j in range(count, len(words)):
        if sorted(i) == sorted(words[j]):
            for s in squares:
                if len(str(s)) == len(str(i)):
                    d = annagram_square(s,i, words[j])
                    if is_square(d):
                        square_set.clear()
                        for x in str(d):
                            square_set.add(x)
                        if len(word_set) == len(square_set):
                            if d > result:
                                result = d
                            if s > result:
                                result = s
print('Result: ', result)


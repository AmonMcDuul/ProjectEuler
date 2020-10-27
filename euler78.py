# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.
import sys 
s = set()
result = 0

def count_number_of_ways_to_sum(n):
    for target_sum in range(2,n):
        if target_sum <= 1:
            raise ValueError('there are no numbers greater than 0 less than the target sum')
        # ith index contains the answer to the (i + 1)th subproblem
        num_ways_to_sum = [0] * (target_sum + 1)
        # There is only 1 way to sum to 1
        num_ways_to_sum[0] = 1
        # Consider sums involving numbers in [1, target_sum)
        for i in range(1, target_sum):
            # Every subproblem j >= i depends on i
            for j in range(i, target_sum + 1):
                # The number of ways to sum j includes all the ways to sum i 
                # with all the ways to sum (j - i) appended (like the parenthesis)
                num_ways_to_sum[j] += num_ways_to_sum[j - i]
                x = num_ways_to_sum[target_sum]+1
                if x %1000000 == 0:
                    result = x
        s.add(num_ways_to_sum[target_sum])

count_number_of_ways_to_sum(500)
print(sorted(s))
print(result)

# result = 0
# for i in range(2,100000):
#     x = count_number_of_ways_to_sum(i)+1
#     if x %1000000 == 0:
#         result = x
#         print(result)
#         sys.exit()



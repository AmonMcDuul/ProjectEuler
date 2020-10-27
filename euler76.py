# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a sum of at least two positive integers?

def count_number_of_ways_to_sum(target_sum):
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
    return num_ways_to_sum[target_sum]

print(count_number_of_ways_to_sum(100))
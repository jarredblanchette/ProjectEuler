# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 * 7
# 15 = 3 * 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
from sympy import primefactors

if __name__ == '__main__':
    i = 1
    run_of_matches = 0

    while run_of_matches < 4:
        is_match = len(primefactors(i)) == 4
        if is_match:
            run_of_matches +=1
        else:
            run_of_matches = 0

        i += 1

    print(i - 4)

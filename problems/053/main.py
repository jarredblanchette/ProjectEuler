# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5 choose 3 = 10.
# In general, n choose r  = n! / r! * (n-r)!, 
# where r <= n, 
# n! = n * (n-1) * ... * 3 * 2 * 1, 
# and 0! = 1.
# 
# It is not until n = 23, that a value exceeds one-million: {23} choose {10} = 1144066.
# How many, not necessarily distinct, values of n choose r  for 1 <= n <= 100, are greater than one-million?

from math import comb
# from functools import cache

# @cache
# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n-1)

# @cache
# def c(n,r):
#     return fac(n) / (fac(r) * fac(n-r))

def combisum(n,r):
    return comb(n,r)

ONE_MILLION = 1_000_000

if __name__ == '__main__':

    acc = 0

    for n in range(1,101):
        for r in range(1,n+1):
            if combisum(n,r) > ONE_MILLION:
                acc +=1

    print(acc)
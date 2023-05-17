# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math
def sieve(primes, numbers_to_sieve):
    numbers_to_sieve = list(numbers_to_sieve)
    s = primes + numbers_to_sieve

    index = 0
    while index < len(s):
        prime = s[index]
        if prime > math.sqrt(max(s)):
            break
        s = list(filter(lambda x: x % prime != 0 or x == prime, s))
        index += 1

    return s

if __name__ == '__main__':
    two_million = 2000000
    primes = [2,3,5,7]
    numbers = range(11,two_million,2)

    p = sieve(primes,numbers)
    print(sum(p))
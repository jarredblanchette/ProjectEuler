# The arithmetic sequence,
# 1487, 4817, 8147,
# in which each of the terms increases by
# 3330,
# is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

from sympy import primerange, sieve

if __name__ == '__main__':
    def are_all_permutations(values):
        ss = [set(str(element)) for element in values]
        return all([ss[0] == e for e in ss])

    for startingPrime in primerange(1000, 9999):
        for offset in range(100, int((9999 - startingPrime) / 2)):
            results = [startingPrime + i * offset for i in range(3)]
            if all([result in sieve for result in results]) and are_all_permutations(results):
                print(results, ''.join([str(i) for i in results]))

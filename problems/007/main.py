# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def sieve(primes, numbers_to_sieve):
    numbers_to_sieve = list(numbers_to_sieve)

    #my kingdom for the filter method to work on filter objects.
    for prime in primes + numbers_to_sieve:
        if prime > max(numbers_to_sieve)/2:
            break
        numbers_to_sieve = list(filter(lambda x: x % prime != 0 or x == prime, numbers_to_sieve))

    return primes,numbers_to_sieve


if __name__ == '__main__':
    table = [2, 3, 5, 7, 11, 13]
    window = 1000
    while len(table) < 10001:
        numbers = list(range(max(table) + 2, max(table) + window, 2))
        table, filtered = sieve(table, numbers)
        table += filtered
    print(table[10000])

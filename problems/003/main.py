# The prime factors of 13195 are 5,7,13,29
# what is the largest prime factor of the number 600851475143

if __name__ == '__main__':
    MAGIC_NUMBER = 600851475143

    candidate_factor = 2
    remaining_number = MAGIC_NUMBER

    # trick here is that numbers are either composite or prime (ie, not composite).
    # Composite numbers are composed of a set of primes,
    # such that the product of those primes equals the composite number.
    # So this will check if increasingly large values are factors of our number.
    # when we have the candidate reaching our remainder (ie, arbitrary number / itself), we've the largest prime factor
    while remaining_number > 1:
        if remaining_number % candidate_factor == 0:
            remaining_number = remaining_number / candidate_factor
        else:
            # implicitly we'll terminate when candidate_factor = remaining_number, ie the highest prime
            candidate_factor = candidate_factor + 1

    print(candidate_factor)

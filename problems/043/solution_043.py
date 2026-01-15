# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9
# in some order, but it also has a rather interesting sub-string divisibility property.
# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
# d_2 * d_3 * d_4 = 406 is divisible by 2
# d_3 * d_4 * d_5 = 063 is divisible by 3
# d_4 * d_5 * d_6 = 635 is divisible by 5
# d_5 * d_6 * d_7 = 357 is divisible by 7
# d_6 * d_7 * d_8 = 572 is divisible by 11
# d_7 * d_8 * d_9 = 728 is divisible by 13
# d_8 * d_9 * d_10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17]
    prime_products = [[f'{(value * prime):03}' for value in range(1, int(987 / prime)) if
                       len(f'{(value * prime):03}') == len(set(f'{(value * prime):03}'))] for prime in primes]


    def get_permitted_values(candidates, blocking_number):
        """Takes a array of candidates and a blocking number as strings.  Returns a filtered array of candidates ensuring:
        1) ensures the digits of the candidate are not in the front of the blocking number, except for the last two elements of the blocking number
        2) if we have a blocking number, the first two digits of each candate match the lst two digits of the blocking number"""
        # I feel like this could be improved with memorisation
        s = [elem for elem in candidates if all([not d in blocking_number[:-2] for d in elem])]
        if blocking_number is not None:
            s = [elem for elem in s if elem[:2] == blocking_number[-2:]]
        return s


    def get_missing_digit(candidate):
        """Tells us what to add to our candidate to make it a 0..9 pandigital, or -1 if no such value could be added.  Candidate must be a length 9 number (ie, 123456789)"""
        if len(set(str(candidate))) != 9:
            return -1

        i = 9
        while str(i) in str(candidate):
            i -= 1
        return i


    def explore(current_possibilities, remaining_primes, matches):
        """Recursively finds the set of pandigitial numbers satisfying the req for PE043."""

        # conceptually this is a tree traversal, where elements are candidates.
        # each level has had a value added, each element is a valid state.
        # It iteratively goes through each option at the current level,
        # and recursively descends layers
        # we save the computation of the first digit until the end
        for current_value in current_possibilities:
            options = get_permitted_values(remaining_primes[0], current_value)

            if len(options) == 0:
                continue

            new_possibilities = [current_value + option[-1] for option in options]

            if len(remaining_primes[1:]) == 0:
                v = int(f'{get_missing_digit(new_possibilities[0])}{new_possibilities[0]}')
                matches.append(v)
                continue

            matches = explore(new_possibilities, remaining_primes[1:], matches)
        return matches


    s = explore(prime_products[0], prime_products[1:], [])
    print(s, sum(s))

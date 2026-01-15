# It was proposed by
# Christian Goldbach
# that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 =  7  + 2 * 1^2
# 15 = 7  + 2 * 2^2
# 21 = 3  + 2 * 3^2
# 25 = 7  + 2 * 3^2
# 27 = 19 + 2 * 2^2
# 33 = 31 + 2 * 1^2
#
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
from enum import Enum, auto
from sympy import sieve


class MonotonicallyIncreasingSet:
    """A wrapper class for values generated from an infinite monotonically increasing function"""

    # TODO: improve this with better handling for starting iteration in the middle of our list.  Currently it inits
    #  the list up to our point of interest, but we could probably handle this better by changing the underlying data
    #  type to a dict n:f(n) and using a binary search

    class Mode(Enum):
        GENERATOR = auto()
        FUNCTION = auto()

    def __init__(self, function_to_create_values, mode: Mode = Mode.GENERATOR):
        """generator_function generates values for our set.  This function is either a generator, supplying values
        when called with no arguments, or a function, which takes an integer n to generate the nth item of our
        infinite monotonically increasing set."""
        self.iter_start_index = 0
        self.values = []
        self.mode = mode
        self.function_to_create_values = function_to_create_values

    def __getitem__(self, item):
        while item > len(self.values):
            self.add_next()
        return self.values[item - 1]

    def __contains__(self, item):
        if len(self.values) == 0:
            self.add_next()

        while item > self.values[-1]:
            self.add_next()

        return item in self.values

    def __iter__(self):
        self.iter_index = self.iter_start_index
        self.iter_start_index = 0
        self.fill_to(self.iter_index)
        return self

    def __next__(self):
        v = self[self.iter_index]
        self.iter_index += 1
        return v

    def add_value(self, p_n):
        self.values.append(p_n)

    def set_iter_start(self, n):
        """Overrides the starting index of the iterator.  Sets the next iterator generated to start from n, rather than 0."""
        self.iter_start_index = n

    def add_next(self):
        """calculate and insert the next pentagonal value"""
        p_n = None
        if self.mode == self.Mode.FUNCTION:
            n = len(self.values) + 1
            p_n = self.function_to_create_values(n)
        elif self.mode == self.Mode.GENERATOR:
            p_n = next(self.function_to_create_values)

        self.add_value(p_n)

    def index_of(self, value):
        if value not in self:
            return -1
        return self.values.index(value)

    def fill_to(self, k):
        """Helper function, expands our tracked values to ensure that int k is less than our largest value"""
        while len(self.values) <= k:
            self.add_next()
        return self[k]


if __name__ == '__main__':
    def odd_composite_generator():
        candidate = 1
        primes = sieve
        while True:
            candidate += 2
            if candidate not in primes:
                yield candidate


    def odd_twice_squares_generator():
        base = 0
        while True:
            base += 1
            yield 2 * (base ** 2)


    odd_composites = MonotonicallyIncreasingSet(odd_composite_generator())
    twice_squares = MonotonicallyIncreasingSet(odd_twice_squares_generator())
    primes = sieve

    for composite in odd_composites:
        found_solution = False
        for prime in primes:
            remainder = composite - prime
            if remainder <= 0:
                break
            if remainder in twice_squares:
                # print(f'{composite} = {prime} + 2 * {int(math.sqrt(remainder/2))}^2')
                found_solution = True
                break
        if not found_solution:
            print(composite)
            break
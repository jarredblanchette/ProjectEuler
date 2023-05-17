# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 ... 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 385 - 3025 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


if __name__ == '__main__':
    first_hundred = range(1, 101)

    square_sum = sum(map(lambda x: x * x, first_hundred))
    sum_square = sum(first_hundred) * sum(first_hundred)

    print(sum_square - square_sum)

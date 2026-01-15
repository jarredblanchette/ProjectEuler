# Starting with the number 1 and moving to the right in a clockwise direction,
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def diagonal(size: int):
    yield 1

    maxYield = (2 * size) - 1
    yielded = 1
    skip = 2
    current = 1

    while yielded < maxYield:
        for _ in range(0, 4):
            current = current + skip
            yielded += 1
            yield current
        skip += 2


if __name__ == '__main__':
    print(sum(diagonal(1001)))

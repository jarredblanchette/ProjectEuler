# The series:
# 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
#
# Find the last ten digits of the series:
# 1^1 + 2^2 + 3^3 + ... + 1000^1000
#


if __name__ == '__main__':
    print(sum(
        [(i ** i) % (10 ** 10) for i in range(1, 1001)]
    ) % (10 ** 10))

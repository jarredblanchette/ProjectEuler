# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
import math

if __name__ == '__main__':
    broke = False

    for c in range(1, 1000):
        for a in range(1, c):
            b = math.sqrt(c * c - a * a)
            if b.is_integer():
                if (a + b + c == 1000):
                    print(a, b, c, a * b * c)
                    broke = True
                    break

            if broke: break
        if broke: break

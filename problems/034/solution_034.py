from functools import cache

@cache
def factorial(n:int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)


# suppose we're given a list of digits
# we should factorial each and add together, then check we use the same digits in our sum
def hasFactorSum(digits:list[int])->int:
    """:returns value if the sum of the facorial of each of the digits reuuses the original digits, else -1"""
    acc = sum([factorial(n) for n in digits])

    sumDigits = [int(n) for n in str(acc)]

    digits.sort()
    sumDigits.sort()

    if digits == sumDigits:
        return acc
    return 0


if __name__ == '__main__':
    acc = []
    # I cannot articulate why, but I feel this is a good upper limit
    for i in range(3,factorial(9)):
        if hasFactorSum([int(n) for n in str(i)]) == i:
            acc.append(i)
    print(acc, sum(acc))
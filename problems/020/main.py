from functools import cache


@cache
def fact(n: int) -> int:
    return n * fact(n - 1) if n else 1


if __name__ == '__main__':
    print(sum([int(c) for c in str(fact(100))]))



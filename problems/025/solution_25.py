from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


class FibIter:
    index: int

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        i = fib(self.index)
        return i


if __name__ == '__main__':
    fi = FibIter()
    value = next(fi)

    while len(str(value)) < 1000:
        value = next(fi)

    print(fi.index)

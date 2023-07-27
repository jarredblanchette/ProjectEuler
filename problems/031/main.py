from functools import cache

@cache
def makeChange(coins: tuple[int], target: int) -> int:
    """Takes a set of available coins and a taget value, returns the number of ways we can make change"""
    # Reason for the weirdness and using of tuples rather than a list is that we want to use caching.
    # Finding change for n is the same problem regardless of what you've done before.
    # IE, if you're making a change for a quid it doesn't matter if you'd started with a tenner or at a quid

    if target <= 0:
        return 1

    coins = [coin for coin in coins if coin <= target]
    coins.sort()

    acc: int = 0
    for coin in coins:
        acc += makeChange(tuple([c for c in coins if c <= coin]), target - coin)
    return acc


if __name__ == '__main__':
    coins = tuple([1, 2, 5, 10, 20, 50, 100, 200])
    print(makeChange(coins, 200))

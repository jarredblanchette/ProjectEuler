# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def next(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


def previous(n):
    if (n - 1) % 3 == 0 and int((n - 1) / 3) % 2 != 0:
        return n * 2, int((n - 1) / 3)
    return n * 2, None

def get_length(n, running = 1, completed = None):
    if completed is None:
        completed = {1: (None, 0)}

    if n in completed:
        return completed[n][1]

    child = next(n)

    total = get_length(child,running ,completed) + 1
    completed[n] = (child,total)

    return total

if __name__ == '__main__':
    MAX_VALUE = 1000000

    completed = { 1: (None, 0)}

    best_length, best_value = -1,-1

    for i in range(1,MAX_VALUE):
        l = get_length(i,1,completed)
        if l > best_length:
            print(best_length,best_value,l,i)
            best_length, best_value = l,i

    print(best_length, best_value)
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of multiples of 3 or 5 below 1000.
def multiples(candidates):
    # pull lambda to own function if needed
    return filter(lambda e: e % 3 == 0 or e % 5 == 0, candidates)

if __name__ == '__main__':
    print(sum(multiples(range(0, 1000))))

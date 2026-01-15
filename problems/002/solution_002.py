# Each new term in the Fibonacci sequence is generate by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13,21,34,55,89

# By considering the terms in the Fibonacci sequence who values do not exceed four million,
# find the sum of the even-valued terms
def fib_add(table, value_limit):
    """computes values of fibbonacci which do not exceed a value.
     :param table: seed table for DP, returns this table filled with values
     :param value_limit: the maximum value for which we will add to our table"""

    if len(table) < 2:
        table = [1,2]

    while (table[-1] + table[-2]) < value_limit:
        table.append(table[-1] + table[-2])

    return table


if __name__ == '__main__':
    FOUR_MILLION = 4000000
    fib = [1, 2]
    fib_add(fib, FOUR_MILLION)
    print(sum(filter(lambda x: x % 2 == 0, fib)))

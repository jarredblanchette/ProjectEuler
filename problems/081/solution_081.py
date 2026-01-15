# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# {131}   673    234    103    18
# {201}   {96}   {342}  965    150
# 630     803    {746}  {422}  111
# 537     699    497    {121}  956
# 805     732    524    {37}   {331}
#
# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt, a 31K text file containing an 80 by 80 matrix.
from functools import cache


def solve(matrix: list[list[int]]):

    @cache
    def costTo(x: int, y: int) -> int:
        acc = matrix[y][x]
        options = []

        if y > 0:
            options.append(costTo(x, y - 1))

        if x > 0:
            options.append(costTo(x - 1, y))

        if options:
            acc += min(options)

        return acc

    return costTo(len(matrix[0]) - 1, len(matrix) - 1)


def generate_matrix(filepath: str) -> list[list[int]]:
    acc: list[list[int]] = []

    with open(filepath, 'r') as file:
        for line in file:
            acc.append([int(i) for i in line.split(',')])

    return acc


if __name__ == '__main__':
    path = '0081_matrix.txt'
    mat = generate_matrix(path)

    print(solve(mat))

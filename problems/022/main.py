# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN,
# which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 times 53 = 49714.
# What is the total of all the name scores in the file?

if __name__ == '__main__':
    acc: int = 0
    lines: list[str] = []
    with open('0022_names.txt', 'r') as file:
        f = file.read()
        lines = f.split(',')
        lines = [l.strip('"') for l in lines]

    lines.sort()

    for index, line in enumerate(lines):
        lineScore = 0
        for c in line:
            lineScore += ord(c) - 64
        lineScore *= index + 1
        acc += lineScore

    print(acc)

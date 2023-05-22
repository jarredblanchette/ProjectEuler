# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


import math
if __name__ == '__main__':
    value = math.pow(2,1000)
    value = str(int(value))
    acc = 0
    for char in value:
        acc += int(char)

    print(acc)
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n: int):
    s = str(n)
    if len(s) % 2 != 0:
        tail = s[-1:-len(s) + 1:-1]
    else:
        tail = s[-1:-int(len(s)/2)-1:-1]
    head = s[0:int(len(s) / 2)]

    return tail == head


if __name__ == '__main__':
    broke = False
    best = -1
    for i in range(999, 0, -1):
        for j in range(i, 0, -1):
            if is_palindrome(i * j) and i*j > best:
                best = i*j
    print(best)

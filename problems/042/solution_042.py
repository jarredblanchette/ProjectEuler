# The nth term of the sequence of triangle numbers is given by, t_n = (1/2) n (n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example, the word value for
# SKY is
# 19 + 11 + 25 = 55 = t_10.
# If the word value is a triangle number then we shall call the word a triangle word
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def triangleGenerator():
    """Returns a function testing if i:int is a triangle number, defined as in the set t(n) = 0.5n(n-1)"""
    triangles = [1]
    n = 2

    def isTriangle(i: int) -> bool:
        nonlocal triangles, n
        while i > triangles[-1]:
            triangles.append((0.5) * n * (n - 1))
            n += 1
        return i in triangles

    return isTriangle


def score_word(word: str) -> int:
    word = word.upper()
    offset = ord('A') - 1  # sub 1 because we're wanting a 1-index value
    return sum([ord(c) - offset for c in word])


if __name__ == '__main__':
    passingWords = []
    isTrangular = triangleGenerator()

    with open('words.txt', 'r') as blob:
        words = []
        for line in blob:
            line = line.split(',')
            [words.append(word.strip('"')) for word in line]

        passingWords = [word for word in words if isTrangular(score_word(word))]

    print(len(passingWords),passingWords)


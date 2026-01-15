from itertools import permutations

if __name__ == '__main__':
    OneMillion = 1000000
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    perms = permutations(digits)

    for index, element in enumerate(perms, 1):
        if index == OneMillion:
            print(''.join([str(i) for i in element]))
            break

# 2520 is the smallest number that can be devided by each of the numbers from 1 to 10 without any remainder
# what is the smallest positive number that is evenly divisable by all the numbers from 1 to 20?

def divisable(candidate, values):
    for value in values:
        if candidate % value != 0:
            return False
    return True



if __name__ == '__main__':
    one_to_twenty = range(2,21)
    candidate = 2

    while not divisable(candidate,one_to_twenty):
        candidate += 2

    print(candidate)
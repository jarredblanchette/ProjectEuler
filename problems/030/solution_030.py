if __name__ == '__main__':

    # todo: this should be improved, or at least check that there's no values larger than 10^7 that satisfy us
    p = 5
    l = ([
        n
        for n in range(2, pow(10, 7))
        if sum([pow(int(d), p) for d in str(n)]) == n
    ])

    print(l, sum(l))

# If p is the perimeter of a right angle triangle with integral length sides,
# {a, b, c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p < 1000, is the number of solutions maximised?

if __name__ == '__main__':
    max_p = 1000

    best = [0,0]
    for p in range(1,max_p):
        candidate_score = 0

        # min c is sqrt(2)-1 % of p ~ 41%, the case where c has the lowest percentage of p is when we have a=1 , b=1, c=sqrt(2)
        # max c is because we could have a "triangle" with two sides of near equal length and a side of len 1
        for c in range(int(0.41 * p),int(p/2)):
            cc = c*c

            # a > b
            # min a is (p-c)/2 +1, ie the minimum value such that a > b and a+b+c = p
            # max a is c -1 for the case where we have two near parallel lines and b = 1
            for a in range(int((p-c)/2),c):
                aa = a*a
                b = p-(a+c)

                if aa +b*b == cc:
                    candidate_score +=1

        if candidate_score > best[0]:
            best = [candidate_score,p]

    print(best)
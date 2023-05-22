# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (
# one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.
def memorise(f):
    known = {}

    def wrapper(*args, **kwargs):
        if (args, str(kwargs)) not in known:
            known[(args, str(kwargs))] = f(*args, **kwargs)
        return known[(args, str(kwargs))]

    return wrapper


@memorise
def get_length(n):
    Units = {1: 'One',
             2: 'Two',
             3: 'Three',
             4: 'Four',
             5: 'Five',
             6: 'Six',
             7: 'Seven',
             8: 'Eight',
             9: 'Nine'}

    Teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 15: 'Fifteen', 18: 'Eighteen'}
    Tens = {1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 8: 'Eighty'}

    for u in Units:
        if u not in Tens:
            Tens[u] = Units[u] + 'ty'
        if u + 10 not in Teens:
            Teens[10 + u] = Units[u] + 'teen'


    if n >= 1000:
        if n % 1000 == 0:
            child = get_length(int(n / 1000))
            return child[0] + len('Thousand'), child[1] + ' thousand'
        children = get_length(int(n / 1000)), get_length(n % 1000)
        # todo: this 'and' logic works for 'Ten thousand and Ten' but not for 'Ten thousand and One hundred' or 'One Hundred and One thousand and Ten'
        # biggest issue is that we can only determine if there should be 'and' with certainty at the bottom. Could flip the adding of 'and' to be for the child?
        return children[0][0] + len('Thousand') + len('and') + children[1][0], children[0][1] + ' thousand and ' + \
               children[1][1]

    if n >= 100:
        if n % 100 == 0:
            child = get_length(int(n / 100))
            return child[0] + len('Hundred'), child[1] + ' hundred'
        children = get_length(int(n / 100)), get_length(n % 100)
        return children[0][0] + len('Hundred') + len('and') + children[1][0], children[0][1] + ' Hundred and ' + \
               children[1][1]

    if n >= 20:
        if n % 10 == 0:
            return len(Tens[int(n / 10)]), Tens[int(n / 10)]
        return len(Tens[int(n / 10)]) + get_length(n % 10)[0], Tens[int(n / 10)] + get_length(n % 10)[1]

    if n < 20 and n > 9:
        return len(Teens[n]), Teens[n]

    if n < 10:
        return len(Units[n]), Units[n]


if __name__ == '__main__':

    acc = 0
    for i in range(1, 1001):
        acc += get_length(i)[0]
    print(acc)

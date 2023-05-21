# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# ─ │
# ━ ┃
#
# ━━━━━━━    ━━━━───    ━━━━───
# │  │  ┃    │  ┃  │    │  ┃  │
# ───────    ────━━━    ───────
# │  │  ┃    │  │  ┃    │  ┃  │
# ──────X    ──────X    ───━━━X

# ───────    ───────   ───────
# ┃  │  │    ┃  │  │   ┃  │  │
# ━━━━━━━    ━━━────   ───────
# │  │  ┃    │  ┃  │   ┃  │  │
# ──────X    ───━━━X   ━━━━━━X
#
# How many such routes are there through a 20×20 grid?


def memorise(f):
    known = {}

    def wrapper(*args):
        if args not in known:
            known[args] = f(*args)
        return known[args]

    return wrapper


@memorise
def routes(width, height):
    if width == 0 or height == 0:
        return 1

    acc = 0

    # this is go right
    acc += routes(width - 1, height)

    # go down
    acc += routes(width, height - 1)

    return acc


if __name__ == '__main__':
    print(routes(20, 20))

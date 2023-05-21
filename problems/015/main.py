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

def routes(width, height, lookup):
    if width == 0 or height == 0:
        return 1,lookup

    if (width,height) in lookup or (height,width) in lookup:
        return (lookup.get((width,height), None) or lookup.get((width,height),None)) , lookup

    acc = 0

    # this is go right
    r,lookup = routes(width-1,height,lookup)
    acc += r

    # go down
    r,lookup = routes(width,height-1,lookup)
    acc += r

    lookup[(width,height)] = acc
    lookup[(height, width)] = acc
    return acc , lookup

if __name__ == '__main__':
    print(routes(20,20,{})[0])

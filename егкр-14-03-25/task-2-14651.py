from itertools import product, permutations
def f(x, y, z, w):
    return (z <= x) == (w <= y) or (x and w)
for a1, a2, a3, a4, a5, a6 in product([1, 0], repeat=6):
    table = [(a1, a2, a3, 1), (a4, a5, 1, 1), (a6, 1, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p)
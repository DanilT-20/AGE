from itertools import product, permutations
def f(x, y, z ,w):
    return (w <= (y == z)) and (y == (z <= x))
for a1, a2 in product([1, 0],repeat=2):
    table = [(a1,0,0,0), (0,a2,1,1), (0,0,0,1)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,0]:
                print(*p)
from itertools import product, permutations
def f(x,y,z,w):
    return not w and ((y or z) <= (not x and y))
for a1,a2,a3,a4,a5,a6,a7,a8 in product([1,0], repeat=8):
    table = [(a1, a2, a3, 1),(a4, a5, 1, a6),(a7, 1, 1, a8)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,1]:
                print(*p)

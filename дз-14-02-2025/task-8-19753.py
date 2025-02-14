def f(alph):
    for x in alph:
        for y in alph:
            u = (x + y) not in v
            if not u:
                return 0
    return 1
alph = '02468'
count = 0
from itertools import permutations
for v in permutations('0123456789', 6):
    v = ''.join(v)
    if int(v) % 4 == 0 and f(alph) and v[0] != '0':
        count += 1
print(count)


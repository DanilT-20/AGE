from itertools import permutations
def f(p):
    for i in p:
        if i in '0246':
            p = p.replace(i, '*')
        else:
            p = p.replace(i, '?')
    if '??' not in p and '**' not in p:
        return 1
    return 0
count = 0
for p in permutations('01234567', 6):
    p = ''.join(p)
    if p[0]!= '0' and int(p, 8)%5==0 and f(p):
        count += 1
print(count)


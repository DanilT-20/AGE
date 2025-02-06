from itertools import permutations
ans = []
for v in set(permutations('ХОЧУНФБЮДЖЕТ')):
    v = ''.join(v)
    for i in v:
        if i in 'ОУАЮЕ':
            v = v.replace(i, 'c')
    if 'ccccc' not in v:
        ans.append(v)
print(len(ans))

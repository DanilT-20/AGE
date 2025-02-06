from itertools import permutations
count = 0
for v in set(permutations('СОТОЧКА')):
    v = ''.join(v)
    if 'ОО' in v or 'ОА' in v or 'АО' in v:
        count += 1
print(count)

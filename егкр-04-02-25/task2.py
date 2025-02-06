from itertools import permutations
count = 0
for v in set(permutations('КИДАЛА', 5)):
    v = ''.join(v)
    if 'АА' not in v:
        count += 1
print(count)


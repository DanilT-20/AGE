from itertools import permutations
def f(n):
    count1 = 0
    for i in range(len(n)-1):
        d = n[i:i+2]
        if d in 'аа аи иа':
            count1 += 1
    if count1 != 1:
        return 0
    return 1
count = 0
for p in set(permutations('парижанка')):
    p = ''.join(p)
    if f(p):
        count += 1
print(count)
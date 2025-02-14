from itertools import product
count = 0
for v in product('ясновидец', repeat=5):
    v = ''.join(v)
    if v[-1] in 'яоие' and v[0] in 'снвдц':
        v1 = v[0]
        v2 = v[-1]
        if v.count(v[0]) == 1 and v.count(v[-1]) == 1:
            count += 1
print(count)
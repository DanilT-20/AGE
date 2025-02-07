from itertools import permutations
count = 0
for v in permutations('хочу в вуз'):
    v = ''.join(v)
    v = v.split()
    count1 = 0
    for i in v:
        if i[0] != 'у':
            count1 += 1
        else:
            count1 -= 4
    if count1 > 0:
        count += 1
print(count)


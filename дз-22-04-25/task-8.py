from itertools import product
def f(n):
    for i in range(len(n)-2):
        m = n[i:i+3]
        if m in [str(x*3) for x in '012345678']:
            return 0
    return 1
count = 0
for p in product('012345678', repeat=7):
    p = ''.join(p)
    if p[-1] not in '347' and f(p) and p[0] != '0':
        count += 1
print(count)
count1 = 0
for p in product('012345678', repeat=7):
    p = ''.join(p)
    if p[-1] not in '347' and p[0]!='0' and len([i for i in [str(x*3) for x in '012345678'] if i in p]) == 0:
        count1 += 1
print(count1)


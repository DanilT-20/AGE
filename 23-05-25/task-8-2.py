from itertools import product
def f1(n):
    ch = []
    for i in '02468':
        for y in '02468':
            ch.append(i+y)
    for i in ch:
        if i in n:
            return 0
    return 1
def f2(n):
    ch = []
    for i in '13579':
        for y in '13579':
            ch.append(i+y)
    for i in ch:
        if i in n:
            return 0
    return 1
ans = []
count = 0
for n in '123456789':
    for v in product('0123456789', repeat=4):
        count += 1
        v = n + ''.join(v)
        if count%15==0 and f1(v) and f2(v):
            ans.append(count)
print(ans[-1])

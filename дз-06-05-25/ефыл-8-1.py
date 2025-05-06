from itertools import product
count = 0
for p in product('012345678', repeat=7):
    p = ''.join(p)
    if p.count('6') >= 1 and p[0] in '2468' and int(p[-1])%3!=0:
        count += 1
print(count)

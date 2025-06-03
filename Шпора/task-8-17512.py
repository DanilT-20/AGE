from itertools import product
count = 0
for p in product('01234567', repeat=5):
    p = ''.join(p)
    if p[0] not in '01357' and p[-1] not in '26' and p.count('7')<=2:
        count += 1
print(count)

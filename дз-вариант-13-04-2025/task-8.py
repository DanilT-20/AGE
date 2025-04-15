from itertools import product
count =0
for p in product('01234', repeat=6):
    p = ''.join(p)
    if p[-1] in '024' and p[0] == '3':
        count += 1
print(count)

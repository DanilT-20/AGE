from itertools import product
count = 0
for p in product('0123456789ABCD', repeat=8):
    p= ''.join(p)
    if p[0]!= 0 and p.count('0') == 2 \
            and sum([1 for i in p if i in 'ABCD']) <= 4:
        count += 1
print(count)
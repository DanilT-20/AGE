from itertools import product
count = 0
for p in product('0123456789ABCDE', repeat=5):
    p = ''.join(p)
    if p.count('8')==1 and p[0]!='0' and len([i for i in p if int(i, 15)>9])>=2:
        count += 1
print(count)
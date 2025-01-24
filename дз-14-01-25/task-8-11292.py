from itertools import product
count = 0
for i in product('0123456789ABCDEF', repeat=5):
    i = ''.join(i)
    for p in '02468ACE':
        if i[0] != '0' and i.count('6') == 2 and p + '6' not in i and '6' + p not in i:
            count += 1
print(count)
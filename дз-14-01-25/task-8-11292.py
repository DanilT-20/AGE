from itertools import product
for i in product('0123456789ABCDEF', repeat=5):
    i = ''.join(i)
    i = [1 for p in ''.join(str(product('02468ACE', repeat=2))) if (i[0] != '0' and i.count('6') == 2 and p not in i)]
print(len(i))
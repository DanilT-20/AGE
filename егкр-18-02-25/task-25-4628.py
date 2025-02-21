# 1 способ

from itertools import product
asn = []
for v in '0123456789':
    for r in range(3):
        for z in product('0123456789', repeat=r):
            z = ''.join(z)
            num1 = int(f'12{z}4{v}65')
            if num1 <= 10**8 and num1 % 161 == 0:
                asn.append([num1, num1//161])
for i in sorted(asn):
    print(*i)

# 2 способ

from fnmatch import fnmatch
for i in range(161, 10**8+1, 161):
    if fnmatch(str(i), '12*4?65'):
        print(i, i//161)

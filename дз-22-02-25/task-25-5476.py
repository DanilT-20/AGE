from itertools import product
from fnmatch import fnmatch
def f(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //=sys
    return res[::-1]
for r in range(12135664 - 12135664 % 333, 10**9, 333):
    if
    for n in range(2):
        for i in product('0123456', repeat=n):
            i = ''.join(i)
            if fnmatch(str(f(r, 7)), f'[!0]213{i}'):
                print(r, r//333)
print('---------------------')
for v in '123456789':
    for r in range(2):
        for z in product('0123456789', repeat=r):
            z = ''.join(z)
            num = f'{v}213{z}5664'

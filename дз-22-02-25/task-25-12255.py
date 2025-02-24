from itertools import product, repeat
from fnmatch import fnmatch
for i in range(1203456009 - 1203456009 % 98591, 10**12, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i//98591)
print('-------------')
ans = []
for v1 in '0123456789':
    for v2 in '0123456789':
        for v3 in '0123456789':
            for r in range(3):
                for z in product('0123456789', repeat=r):
                    z = ''.join(z)
                    num = int(f'12{v1}3{z}456{v2}{v3}9')
                    if num <= 10**12 and num % 98591 == 0:
                        ans.append([num, num//98591])
ans = sorted(ans)
for i in ans:
    print(*i)

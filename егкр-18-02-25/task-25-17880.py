# 1 способ

from itertools import product
ans = []
for v1 in '0123456789':
    for v2 in '0123456789':
        for r in range(3):
            for z in product('0123456789', repeat = r):
                z = ''.join(z)
                num = int(f'3{v1}12{v2}14{z}5')
                if num <= 10**10 and num % 1917 == 0:
                    ans.append([num, num//1917])
for i in sorted(ans):
    print(*i)


from fnmatch import fnmatch
for i in range(30120145 - 30120145 % 1917, 10**10+1, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i//1917)
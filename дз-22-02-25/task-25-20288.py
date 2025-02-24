from itertools import product
from fnmatch import fnmatch
for i in range(12040 - 12040 % 9231, 10**10, 9231):
    if fnmatch(str(i), '[!0]*12[13579]4[13579]'):
        print(i, i//9231)
print('-----------------------')
ans = []
for v1 in '13579':
    for v2 in '13579':
        for r in range(6):
            for z in product('02468', repeat=r):
                z = ''.join(z)
                num = f'{z}12{v1}4{v2}'
                if num[0] != '0':
                    if int(num) <= 10**10 and int(num) % 9231 == 0:
                        ans.append([int(num), int(num)//9231])
ans = sorted(ans)
for i in ans:
    print(*i)

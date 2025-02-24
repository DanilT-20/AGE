from itertools import product
from fnmatch import fnmatch
ans = []
ans1 = []
for i in range(1157424 - 1157424 % 111, 10**8, 111):
    if fnmatch(str(i), '*15*7424'):
        ans.append([i, i//111])
for i in range(1157424 - 1157424 % 113, 10**8, 113):
    if fnmatch(str(i), '*15*7424'):
        ans.append([i, i//113])
for i in range(1157424 - 1157424 % 127, 10**8, 127):
    if fnmatch(str(i), '*15*7424'):
        ans.append([i, i//127])
ans = sorted(ans)
for i in ans:
    print(*i)
print('--------------------')
for r1 in range(3):
    for r2 in range(3-r1):
        for z1 in product('123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                z2 = ''.join(z2)
                z1 = ''.join(z1)
                num = int(f'{z1}15{z2}7424')
                if (num % 111 == 0) + (num % 113 == 0) + (num % 127 == 0) == 1 and num <= 10**8:
                    if num % 111 == 0:
                        ans1.append([num, num//111])
                    if num % 113 == 0:
                        ans1.append([num, num //113])
                    if num % 127 == 0:
                        ans1.append([num, num //127])
ans1 = sorted(ans1)
for i in ans1:
    print(*i)














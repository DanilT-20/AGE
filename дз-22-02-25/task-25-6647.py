from itertools import product
from fnmatch import fnmatch
for i in range(1021394 - 1021394 % 3052, 10**10, 3052):
    if fnmatch(str(i), '1?2139*4'):
        print(i, i//3052)
print('--------------------')
ans = []
for v1 in '0123456789':
    for r in range(4):
        for z in product('0123456789', repeat=r):
            z = ''.join(z)
            num = int(f'1{v1}2139{z}4')
            if num % 3052 == 0 and num <= 10**10:
                ans.append([num, num//3052])


ans = sorted(ans)
for i in ans:
    print(*i)

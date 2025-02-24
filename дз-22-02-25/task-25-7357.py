from itertools import product
from fnmatch import fnmatch
ans = []
ans1 = []
for r in range(53191, 10**10, 53191):
    if fnmatch(str(r), '[2468]136[13579][13579][13579][13579][13579][13579]'):
        ans1.append([r, r//53191])
ans1 = sorted(ans1)
for i in ans1[-5:]:
    print(*i)
print('--------------------')
for v in '2468':
    for r in range(7):
        for z in product('13579', repeat=r):
            z = ''.join(z)
            num = int(f'{v}136{z}')
            if num <= 10**10 and num % 53191 == 0:
                ans.append([num, num//53191])
ans = sorted(ans)
for i in ans[-5:]:
    print(*i)

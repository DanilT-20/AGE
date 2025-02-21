from itertools import product
ans = []
for a in '02468':
    for i in range(4):
        for b in product('13579', repeat=i):
            b = ''.join(b)
            num = int(f'1{a}2157{b}4')
            if num <= 10**10 and num % 133 == 0:
                ans.append([num, num // 133])
ans = sorted(ans)
for i in ans:
    print(*i)
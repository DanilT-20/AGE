from itertools import product
ans = []
for z in '0123456789':
    for r in range(4):
        for v in product('0123456789', repeat=r):
            v = ''.join(v)
            num = int(f'85{z}16{v}4')
            if num <= 10**9 and num % 2658 == 0:
                ans.append([num, num//2658])
ans = sorted(ans)
for i in ans:
    print(*i)
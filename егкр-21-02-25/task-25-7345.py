from itertools import product
ans = []
for r1 in range(6):
    for r2 in range(6 - r1):
        for z1 in product('0123456789', repeat=r1):
            z1 = ''.join(z1)
            for z2 in product('0123456789', repeat=r2):
                z2 = ''.join(z2)
                num = int(f'8{z1}80{z2}06')
                if num % 4546 == 0 and num <= 10**10:
                    ans.append([num, num//4546])
ans = sorted(ans)
for i in ans[::61]:
    print(*i)
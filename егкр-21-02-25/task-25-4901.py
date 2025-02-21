from itertools import product
ans = []
for v1 in '123456789':
    for v2 in '0123456789':
        for r1 in range(3):
            for r2 in range(3):
                for z1 in product('0123456789', repeat=r1):
                    z1 = ''.join(z1)
                    for z2 in product('0123456789', repeat=r2):
                        z2 = ''.join(z2)
                        num = int(f'{v1}6{z1}6{z2}{v2}6')
                        if num % 6 == 0 and num % 7 == 0 and num % 8 == 0:
                            ans.append([num, ])
ans = sorted(ans)
for i in ans:
    print(*i)
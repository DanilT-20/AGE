from itertools import product
ans = []
for v in '0123456789':
    for r in range(5):
        for z in product('0123456789', repeat=r):
            z = ''.join(z)
            num = int(f'12{z}34{v}5')
            if num <= 10**10 and num % 21025 == 0:
                ans.append([num, num//21025])
ans = sorted(ans)
for i in ans:
    print(*i)
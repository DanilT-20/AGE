from itertools import product
ans = []
for r in range(3):
    for r1 in range(3):
        for z in product('0123456789', repeat=r):
            z = ''.join(z)
            for z1 in product('0123456789', repeat=r1):
                z1 = ''.join(z1)
                num = f'124{z}5{z1}79'
                summ = 0
                for i in num:
                    if int(i) % 2 != 0:
                        summ += int(i)
                if int(num) <= 10**8 and int(num) % summ == 0:
                    ans.append([num, sum(map(int, num))])
ans = sorted(ans)
for i in ans:
    print(*i)



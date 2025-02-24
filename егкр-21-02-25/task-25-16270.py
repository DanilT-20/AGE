
ans = []
for v1 in '0123456789':
    for v2 in '0123456789':
        for v3 in '0123456789':
            num = int(f'12{v1}345{v2}67089{v3}')
            if num <= 10**13 and num % 206 == 0:
                ans.append([num, num//206])
ans = sorted(ans)
for i in ans:
    print(*i)
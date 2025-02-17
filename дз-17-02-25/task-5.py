def f(n, s):
    res = ''
    while n:
        res += str(n % s)
        n //= s
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = f(n, 4)
    if len(r)%2 == 0:
        if len(r) == 2:
            r = r[0] + '0' + r[-1]
        else:
            r = r[:len(r)//2 + 1] + '0' + r[:len(r)//2 + 1:-1]
    r = int(r, 4)
    if r <= 180:
        ans.append(n)
print(max(ans))



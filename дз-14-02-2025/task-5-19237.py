def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 1000):
    r = f(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + f(sum(map(int, r)), 3)
    r = int(r, 3)
    if r > 220 and r % 2 == 0:
        ans.append(r)
print(min(ans))


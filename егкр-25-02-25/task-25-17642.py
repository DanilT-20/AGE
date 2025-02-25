def f(num):
    res = set()
    for r in range(2, int(num**0.5) + 1):
        if num % r == 0:
            res |= {r, num//r}
    res = sorted(res)
    for i in res:
        if str(i)[-1] == '9' and i != 9:
            return i
    return 0
count = 0
for i in range(800001, 10**15):
    n = f(i)
    if n:
        print(i, n)
        count += 1
        if count == 5:
            break

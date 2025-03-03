def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    if len(res) >= 2:
        m = min(res) + max(res)
        if str(m)[-1] == '4':
            return m
    return 0
count = 0
for r in range(800001, 10**15):
    n = f(r)
    if n:
        print(r, n)
        count += 1
        if count == 5:
            break
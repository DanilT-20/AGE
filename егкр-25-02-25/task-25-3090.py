def f1(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1
def f(num):
    res = set()
    for r in range(1, int(num**0.5)+1):
        if num % r == 0:
            res |= {r, num//r}
    res = sorted(res)
    p = [i for i in res if f1(i)]
    n = [i for i in res if i % 2 == 0]
    m = abs(sum(p) - sum(n))
    if len(p) == len(n):
        return m
    return 0
count = 0
for r in range(100000001, 10**15):
    x = f(r)
    if x:
        print(r, x)
        count += 1
        if count == 5:
            break


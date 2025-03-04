def f(num):
    res = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    s = 0
    p = 1
    if len(res) > 10:
        s = sum(res)
        for i in res:
            p = p*i
        if s % 2 != 0 and p % 2 != 0:
            return len(res)
    return 0
count = 0
for i in range(800001, 10**15):
    n = f(i)
    if n:
        print(i, n)
        count += 1
        if count == 6:
            break
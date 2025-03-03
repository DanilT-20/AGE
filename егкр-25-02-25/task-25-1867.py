def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    for i in res:
        if str(i)[-1] == '8' and i != 8:
            return i
    return 0
count = 0
for n in range(500001, 10000000000):
    m = f(n)
    if m:
        print(n, m)
        count += 1
        if count == 5:
            break
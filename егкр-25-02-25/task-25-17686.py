def f(num):
    res = set()
    for r in range(2, int(num**0.5)+1):
        if num % r == 0:
            res |= {r, num//r}
    res = sorted(res)
    for i in res:
        if str(i)[-1] == '7' and i != 7:
            return i
    return 0
count = 0
for i in range(700001, 10**20):
    n = f(i)
    if n:
        print(i, i//n)
        count += 1
        if count == 5:
            break
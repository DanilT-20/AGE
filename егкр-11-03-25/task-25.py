def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            res |= {i, num//i}
    res = sorted([i for i in res if i % 2 != 0])
    if len(res) < 6:
        return 0
    return res[-6]
count = 0
for i in range(200000001, 10**20):
    d = f(i)
    if d:
        print(i, d)
        count += 1
        if count == 5:
            break


def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and i % 2 != 0:
            res |= {i, num//i}
    res = sorted(res)[::-1]
    if len(res) < 6:
        d = 0
    else:
        d = res[5]
    return d
count = 0
for i in range(200000001, 1000**7):
    n = f(i)
    if n:
        print(i, n)
        count += 1
        if count == 5:
            break


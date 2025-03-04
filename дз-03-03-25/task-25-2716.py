def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 and i <= num//2:
            res |= {i, num//i}
    res = sorted(res)
    if len(res) > 2:
        s = sum(res[-3:])
        if s != num and s % 2022 == 0:
            return s
    return 0
count = 0
for i in range(1200001)[::-1]:
    n = f(i)
    if n:
        print(i, n)
        count += 1
        if count == 5:
            break
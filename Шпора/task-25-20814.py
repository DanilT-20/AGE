def f(num):
    res = set()
    for i in range(2, int(num**0.5) +1):
        if num % i==0:
            res|={i, num//i}
    res = sorted(res)
    return sum(res)
count = 0
for i in range(500001, 10**20):
    m = f(i)
    if str(m)[-1]=='9':
        print(i, m)
        count += 1
        if count == 5:
            break
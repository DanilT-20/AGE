def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            res|={i, num//i}
    res = sorted(res)
    if len(res)>=2:
        return min(res) + max(res)
    return 0
count = 0
for i in range(700001, 10**20):
    m = f(i)
    if str(m)[-1] == '4':
        print(i, m)
        count += 1
        if count == 5:
            break
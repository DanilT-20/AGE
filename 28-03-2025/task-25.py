def isp(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    if res: return 0
    return 1
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            res |= {i, num//i}
    res = sorted(res)
    if len(res)>0:
        return sum(res)
    return 0
count = 0
for i in range(1273548, 10**20):
    m = f(i)
    n = m%100000
    if m and isp(n):
        print(i, m)
        count += 1
        if count == 5:
            break
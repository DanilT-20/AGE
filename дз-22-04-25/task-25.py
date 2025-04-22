def f1(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num %i==0:
            res |= {i, num//i}
    res = sorted(res)
    if res:
        return sum(res)
    return 0
count = 0
for i in range(1273547, 10**20):
    m = f(i)
    if f1(m%100000):
        print(i, m)
        count += 1
        if count == 5:
            break
def is_prime(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    if len(res) == 0:
        return 1
    return 0
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            res |= {i, num//i}
    res = sorted(res)
    summ = sum([i for i in res if is_prime(i)])
    if summ > 0 and summ%145==0:
        return summ
    return 0
count = 0
for x in range(32500000, 10**20):
    s = f(x)
    if s:
        print(x, s)
        count += 1
        if count == 7:
            break


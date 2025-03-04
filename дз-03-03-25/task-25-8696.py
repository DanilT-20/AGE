def isprime(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    m = sum(res)
    if isprime(m % 100000):
        return m
count = 0
for i in range(1273547, 10**15):
    n = f(i)
    if n:
        print(i, n)
        count += 1
        if count == 5:
            break


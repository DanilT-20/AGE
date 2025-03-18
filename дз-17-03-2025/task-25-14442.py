from fnmatch import fnmatch
def f(num):
    res = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    n = [i for i in res if fnmatch(str(i), '*7?')]
    if len(n) >= 18:
        return sum(n)
    return 0
for i in range(400000, 500001):
    n = f(i)
    if n:
        print(i, n)

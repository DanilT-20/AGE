from fnmatch import fnmatch
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    if len([i for i in res if fnmatch(str(i), '4*')]) == 24 and fnmatch(str(max(res)), '4*'):
        return max(res)
    return 0
for i in range(10**6):
    n = f(i)
    if n:
        print(i, n)
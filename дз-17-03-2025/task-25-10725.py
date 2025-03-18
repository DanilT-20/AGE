from fnmatch import fnmatch
def f(num):
    res = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted([i for i in res if i %2==0])
    if len(res) >= 4:
        return sum(res)
    return 0
count = 0
for i in range(69750, 10**20):
    n = f(i)
    if fnmatch(str(i), '6*97*5?') and n:
        print(i, n)
        count += 1
        if count == 7: break
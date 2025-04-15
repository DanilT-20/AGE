from fnmatch import fnmatch
def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            res|={i, num//i}
    res = sorted(res)
    if len(res) == 18:
        return max(res)
    return False
for i in range(12045, 10**7):
    if f(i) and fnmatch(str(i), '12?*45'):
        print(i, f(i))

def f(n, m):
    return n%m==0
def fa(a):
    for x in range(1, 10000):
        n = f(a, 12) and (f(530, x) <= ((not(f(a,x))) <= (not(f(170,x)))))
        if not(n):
            return 0
    return 1
count = 0
for a in range(1, 1001):
    if fa(a):
        count += 1
print(count)
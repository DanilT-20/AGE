def f1(n, m):
    return n%m==0
def f(a):
    for x in range(1, 1000):
        if not((f1(x, 2) <= (not(f1(x, 3)))) or (x + a >= 80)):
            return 0
    return 1
for a in range(1, 1000):
    if f(a):
        print(a)
        break

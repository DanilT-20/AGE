def f1(n, m):
    return n%m==0
def f(a):
    for x in range(1, 1000):
        if not(f1(x, a) or ((70 <= x <= 90) <= (not(f1(x, 22))))):
            return 0
    return 1
for a in range(1, 1000)[::-1]:
    if f(a):
        print(a)
        break

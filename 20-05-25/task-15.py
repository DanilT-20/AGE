def f1(a, b, s):
    return a*b > s
def f(c):
    for x in range(1, 3000):
        for y in range(1, 3000):
            h = (not(f1(x, y, c+13))) <= (f1(28, y, 520) or f1(x, 25, 800))
            if not(h):
                return 0
    return 1
for a in range(-3000, 3000)[::-1]:
    if f(a):
        print(a)
        break
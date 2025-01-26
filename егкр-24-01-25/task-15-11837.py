def f(A):
    for x in range(10000):
        for y in range(10000):
            f = (x**2 + y**2 > 1024 - x) or (y < -2*x + A)
            if not f:
                return False
    return 1
for A in range(10000):
    if f(A):
        print(A)
        break
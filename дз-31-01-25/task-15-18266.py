def f(A):
    for x in range(1, 1000):
        t = x&57 == 0 or (x&23 == 0 <= (not(x&A == 0)))
        if not t:
            return 0
    return 1
for A in range(1, 1000):
    if f(A):
        print(A)
        break


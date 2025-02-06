def f(A):
    for x in range(1000):
        d = ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & A == 0))
        if not d:
            return 0
    return 1
for A in range(1000):
    if f(A):
        print(A)
        break
def f(a):
    for x in range(500):
        for y in range(500):
            n = (x<7) or (y>=3*x+a-20) or (x>=34) or (y<121)
            if not n:
                return 0
    return 1
for a in range(500)[::-1]:
    if f(a):
        print(a)
        break
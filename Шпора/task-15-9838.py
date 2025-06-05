def f(a):
    for x in range(400):
        for y in range(400):
            if not((x + 2*y > a) or (y < x) or (x < 30)):
                return 0
    return 1
for a in range(1000)[::-1]:
    if f(a):
        print(a)
        break
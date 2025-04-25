def f(a):
    for x in range(1000000):
        b = ((x&8375 != 0) or (x&6743!=0)) <= (x&a>0)
        if not b:
            return 0
    return 1
for a in range(1, 1000000):
    if f(a):
        print(a)
        break
def fu(a):
    for x in range(100):
        for y in range(100):
            f = (x>=11) or (3*x<y) or (x*y<a)
            if not f:
                return 0
    return 'igor'
for a in range(1000):
    if fu(a):
        print(a)
        break

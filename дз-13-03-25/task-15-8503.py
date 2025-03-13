def f(a):
    for x in range(1000):
        n = ((x&52!=0)and (x&36==0))<= (not(x&a==0))
        if not n:
            return 0
    return 1
for a in range(1000):
    if f(a):
        print(a)
        break

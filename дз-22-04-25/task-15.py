def f(a):
    for x in range(1000):
        for y in range(1000):
            n = ((a<x) or ((x**2-7*x+10) > 0)) and ((a >=y) or ((y**2+7*y+12)>0))
            if not n:
                return 0
    return 1
count = 0
for n in range(1000):
    if f(n):
        count += 1
print(count)

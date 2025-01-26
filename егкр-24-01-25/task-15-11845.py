def f(A):
    for x in range(1, 11112):
        for y in range(1, 11112):
            f = (A % x == 0) <= (x == A) or (x == 1)
            if not f:
                return 0
    return 1
count = 0
for A in range(1, 11112):
    if f(A):
        count += 1
print(count)


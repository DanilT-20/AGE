from itertools import product
for N in product('1234567890', repeat=5):
    N = ''.join(N)
    R = (int(max(N)) + int(min(N))) ** 2
    M = 1
    for p in N:
        if int(p) % 2 == 0:
            M = M * int(p)
    if R > M:
        c = str(R) + str(M)
    else:
        c = str(N) + str(R)
    if c == '12116':
        print(N)
        break

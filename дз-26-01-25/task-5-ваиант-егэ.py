ans = []
def f(n, s):
    res = ''
    while n:
        res += str(n % s)
        n //= s
    return res[::-1]
for N in range(1, 10000):
    R = f(N, 3)
    if N % 3== 0:
        R = R + R[len(R) - 2:]
    else:
        R = R + f((N % 3) * 5, 3)
    R = int(R, 3)
    if R > 133:
        ans.append(R)
print(min(ans))
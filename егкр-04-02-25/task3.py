from string import digits, ascii_uppercase
ans = []
def conv(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
for N in range(1, 10000):
    R = conv(N, 12)
    if N % 3 == 0:
        R = '1' + R + 'B'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)
print(max(ans))


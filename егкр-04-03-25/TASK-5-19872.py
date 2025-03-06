def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 1001):
    r = convert(n, 7)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r1 = r[0]
        r2 = r[-1]
        r = r[1:-1]
        r = r2 + r + r1 + '15'
    while r[0] == '0':
        r = r[1:]
    if len(r) == 4:
        print(n)



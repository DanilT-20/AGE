def f(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]
for n in range(1, 10000):
    r = f(n, 3)
    if sum(map(int, r))%2==0: r = '12' + r[2:]+'0'
    else: r = '10'+r[2:]+'2'
    if int(r,3) > 105:
        print(n)
        break
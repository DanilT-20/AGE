for x in range(1, 2006)[::-1]:
    num = 43**56+113**841-x
    res = ''
    while num:
        res += str(num%4)
        num //= 4
    if res.count('2') <= 712 and len([i for i in res if i in '02'])%2==0 \
        and len([i for i in res if i in '13'])%2==0:
        print(x)
        break


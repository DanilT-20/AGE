def f(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]
for x in range(1, 1000):
    num = f(7**666 + 7 ** 333 + 49**x - 343, 7)
    if num.count('6') == 49:
        print(x)
        break
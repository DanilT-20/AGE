def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            res|={i, num//i}
    res = sorted(res)
    if len(res) != 0:
        m = sum(res)//len(res)
        return m
    return 0
count = 0
for x in range(1, 700000)[::-1]:
    m = f(x)
    if str(m)[-3:] == '313':
        print(x, m)
        count += 1
        if count == 7:
            break
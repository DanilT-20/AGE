def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    if len(res) > 1:
        return min(res) + max(res)
    return ''
count = 0
for i in range(220001, 10**20):
    m = f(i)
    if m and m % 10 == 4:
        print(i, m)
        count +=1
        if count == 5:
            break
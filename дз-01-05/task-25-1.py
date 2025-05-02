alph = [2**i for i in range(1, 100)]
def f(num):
    res = set()
    res |= {num}
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res|={i,num//i}
    res = sorted(res)
    if len([i for i in res if i in alph]) >= 20:
        return res
    return 0
count = 0
for i in range(10**6, 10**22):
    n = f(i)
    if n:
        print(i, sum(m for m in n if int(m) not in alph and int(m) != i))
        count += 1
        if count == 5:
            break
def f1(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1
def f(num):
    res = set()
    for i in range(2, int(num**0.5) +1):
        if num%i==0:
            if f1(i):
                res|={i}
            if f1(num//i):
                res|={num//i}
    res = sorted(res)
    if len(res) >= 1:
        return sum(res)
    return 0
count = 0
for i in range(32500001, 10**20):
    m = f(i)
    if m!=0 and m%145==0:
        print(i, m)
        count += 1
        if count == 7:
            break
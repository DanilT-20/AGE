def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0: res|={i, num//i}
    res = sorted(res)
    res_7 = [i for i in res if i != 7 and str(i)[-1] == '7']
    if len(res_7) != 0:
        return min(res_7)
    return 0
count = 0
for i in range(1125001, 10**20):
    m = f(i)
    if m:
        print(i, m)
        count += 1
        if count == 5:
            break
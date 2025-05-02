def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num %i == 0:
            res |= {i, num//i}
    res = sorted(res)
    if res and max(res)%7==0:
        return max(res)
    return 0
count = 0
for i in range(10**9, 10**20):
    if str(i) == str(i)[::-1] and f(i):
        count += 1
        print(i, f(i))
        if count == 5:
            break


def f(num,end):
    if num == end: return 1
    if num > end or num == 17: return 0
    return f(num+1,end) + f(num*2,end)
print(f(1,10) * f(10,35))

def f(num, end):
    if num == end: return 1
    if num > end or num == 21: return 0
    return f(num+2, end)+f(num+3, end)+f(num*2, end)
print(f(7, 14)*f(14, 32))
def f(num, end):
    if num == end: return 1
    if num > end or num == 8: return 0
    return f(num+3, end) + f(num*2, end)
print(f(2, 32)*f(32,76))

def f(num, end):
    if num == end: return 1
    if num < end: return 0
    return f(num-2, end) + f(num//2, end)
print(f(32, 14)*f(14, 1))
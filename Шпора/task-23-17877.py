def f(num, end):
    if num == end: return 1
    if num < end: return 0
    return f(num-2, end) + f(num//2, end)
print(f(38, 16)*f(16,2))
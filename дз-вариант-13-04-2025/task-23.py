def f(num, end):
    if num == end: return 1
    if num < end or num == 24: return 0
    return f(num-1, end)+f(num-6, end)+f(num//2, end)
print(f(34, 29)*f(29, 19)*f(19,6))

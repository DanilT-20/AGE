def f(num, end):
    if num == end: return 1
    if num >end: return 0
    if num**2 != end:
        return f(num+2, end)+f(num+5, end)+f(num**2, end)
    if num**2 == end:
        return f(num+2, end)+f(num+5, end)
print(f(4, 36))
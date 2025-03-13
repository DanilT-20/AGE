def f(num, end):
    if num < end:
        return 0
    if num == end:
        return 1
    return f(num -2, end) + f(num//2, end)
print(f(28, 10) * f(10, 1))
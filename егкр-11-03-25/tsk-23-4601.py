def f(num, end):
    if num < end:
        return 0
    if num == end:
        return 1
    return f(num - 1, end) + f(num // 2, end)
print(f(30, 12) * f(12, 1))
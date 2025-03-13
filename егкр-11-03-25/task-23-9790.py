def f(num, end):
    if num == end:
        return 1
    if num < end or num == 9 or num == 16:
        return 0
    return f(num - 1, end) + f(num - 2, end) + f(num//3, end)
print(f(19, 3))
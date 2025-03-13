def f(num, end):
    if num == end:
        return 1
    if num > end:
        return 0
    return f(num+1, end) + f(num+2, end) + f(num+3, end)
print(f(5, 7)*f(7, 11))
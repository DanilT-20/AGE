def f(num, end):
    if num == end:
        return 1
    if num < end or num == 7:
        return 0
    return f(num-1, end) + f(num-3,end) + f(num//2,end)
print(f(19, 10)* f(10, 3))
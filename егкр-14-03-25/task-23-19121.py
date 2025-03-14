def f(num, end):
    if num == end:
        return 1
    if num < end:
        return 0
    return f(num-3,end) + f(num//3,end)
print(f(35,8)*f(8,1))
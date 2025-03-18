def f(num, end, cnt=0):
    if num == end:
        return 1
    if num > end:
        return 0
    if num **0.5:
        return 0
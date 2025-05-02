from fnmatch import fnmatch
def f(n):
    for i in range(1, n):
        if i**2 == n:
            return 1
    return 0
for i in range(1746008 - 1746008%86513, 10**12, 86513):
    if fnmatch(str(i), '17*46??8') and f(sum(map(int, str(i)))):
        print(i, i//86513)


from fnmatch import fnmatch
for i in range(392404 - 392404%7058, 10**8, 7058):
    if fnmatch(str(i), '392*4?4*'):
        print(i, i//7058)
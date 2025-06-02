with open('26_3230.txt') as file:
    N = int(file.readline())
    p = [list(map(int, s.split())) for s in file]
p = sorted(p, key=lambda x: [-x[0], x[1]])
minn = [100000, 100000]
for u1, u2 in zip(p, p[1:]):
    if u1[0] == u2[0] and u2[1]-u1[1]-1 == 11:
        minn = min(minn, [u1[1]+1, u1[0]])
print(minn[::-1])
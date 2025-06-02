with open('26_3586.txt') as file:
    N = int(file.readline())
    p = [list(map(int, s.split())) for s in file]
p = sorted(p, key=lambda x: [x[0], x[1]])
maxx = [0, 0]
for u1, u2 in zip(p, p[1:]):
    if u1[0] == u2[0]:
        maxx = max(maxx, [u2[1]-u1[1]-1, u1[0]])
print(maxx[::-1])
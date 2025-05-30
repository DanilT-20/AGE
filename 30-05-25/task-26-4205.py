with open('26_4205.txt') as file:
    N = int(file.readline())
    p = [list(map(int, s.split())) for s in file]
p = sorted(p, key=lambda x: (-x[0], x[1]))
for i in range(N-1):
    u1, u2 = p[i:i+2]
    if u1[0] == u2[0] and u2[1]-u1[1]-1==13:
        print(u1[0], u1[1]+1)
        break
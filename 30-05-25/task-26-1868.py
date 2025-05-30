with open('26_1868.txt') as file:
    N = int(file.readline())
    p = [list(map(int, s.split())) for s in file]
p = sorted(p, key=lambda x: [-x[0], x[1]])
for i in zip(p, p[1:]):
    if i[1][0] == i[0][0]:
        if i[1][1] - i[0][1] - 1 == 2:
            print([i[0][1]+1, i[0][0]][::-1])
            break
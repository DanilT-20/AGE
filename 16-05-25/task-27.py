from math import dist
def f(cl):
    dis = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        dis.append([sum_dist, dot1])
    return min(dis)[1]
with open('27_A_18884.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 2
cls = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cl.append(dot2)
    cls.append(cl)
centrs = [f(c) for c in cls]
sx = sum(c[0] for c in centrs)/len(centrs)
sy = sum(c[1] for c in centrs)/len(centrs)
print(int(abs(sx)), int(abs(sy)))
with open('27_B_18884.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(int, i.split())
        if x > 200:
            cl1.append([x, y])
        elif x < -200:
            cl2.append([x, y])
        else:
            cl3.append([x, y])
centrs = [f(cl1), f(cl2), f(cl3)]
sx = sum(c[0] for c in centrs)/len(centrs)
sy = sum(c[1] for c in centrs)/len(centrs)
print(int(abs(sx)), int(abs(sy)))

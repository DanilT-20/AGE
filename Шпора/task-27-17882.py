from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist+=dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27_A_17882.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 1.5
cls = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                cl.append(dot2)
                data.remove(dot2)
    cls.append(cl)
centrs = [f(cl) for cl in cls]
px = sum(c[0] for c in centrs)/len(centrs)
py = sum(c[1] for c in centrs)/ len(centrs)
print(int(px*10000), int(py*10000))

with open('27_B_17882.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if x <5 and y > 6:
            cl1.append([x, y])
        elif x > 5:
            cl2.append([x, y])
        else: cl3.append([x, y])
centrs = [f(c) for c in [cl1, cl2, cl3]]
px = sum(c[0] for c in centrs)/len(centrs)
py = sum(c[1] for c in centrs)/len(centrs)
print(int(px*10000), int(py*10000))

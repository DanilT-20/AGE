from math import dist
def f(cl):
    distnce = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distnce.append([sum_dist, dot1])
    return min(distnce)[1]
with open('27.13.A_19567.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 1
cls = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cl.append(dot2)
    cls.append(cl)
centrs = [f(cl) for cl in cls]
px = sum(centr[0] for centr in centrs)/len(centrs)
py = sum(centr[1] for centr in centrs)/len(centrs)
print(int(px*10000), int(py*10000))
with open('27.13.B_19567.txt') as file:
    data = [list(map(float, s.replace(',', ',').split())) for s in file]
eps = 0.5
cls = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cl.append(dot2)
    cls.append(cl)
centrs = [f(cl) for cl in cls]
px = sum(centr[0] for centr in centrs)/len(centrs)
py = sum(centr[1] for centr in centrs)/len(centrs)
print(int(px*10000), int(py*10000))

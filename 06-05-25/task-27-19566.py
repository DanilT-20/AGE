from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist+=dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return max(distance)[1]
with open('27.17.A_19566.txt') as file:
    data = [list(map(float, s.replace(',', ',').split())) for s in file]
eps = 1
clusters = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cl.append(dot2)
    clusters.append(cl)
centrs = [f(cl) for cl in clusters if len(cl)>100]
print(int(sum(cl[0] for cl in centrs)/len(centrs)*10000), int(sum(cl[1] for cl in centrs)/len(centrs)*10000))
with open('27.17.B_19566.txt') as file:
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
cnt = [f(cl) for cl in cls if len(cl)>100]
print(int(sum(cn[0] for cn in cnt)/len(cnt)*10000), int(sum(cn[1] for cn in cnt)/len(cnt)*10000))
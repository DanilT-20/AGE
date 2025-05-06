from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist+=dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27A_18623.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 1
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
centers = [f(cluster) for cluster in clusters]
px = sum(centr[0] for centr in centers)/len(centers)
py = sum(centr[1] for centr in centers)/len(centers)
print(int(px*100000), int(py*100000))
with open('27B_18623 (1).txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 1
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
centrs = [f(cluster) for cluster in clusters]
px = sum(cn[0] for cn in centrs)/len(centrs)
py = sum(cn[1] for cn in centrs)/len(centrs)
print(int(px*100000), int(py*100000))
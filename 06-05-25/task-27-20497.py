from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return max(distance)[1]
with open('27.19.A_20497.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps= 0.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
centrs = [f(cluster) for cluster in clusters if len(cluster)>100]
centrtx = sum(centr[0] for centr in centrs)/len(centrs)
centrty = sum(centr[1] for centr in centrs)/len(centrs)
print(centrtx*10000, centrty*10000)
with open('27.19.B_20497.txt.crdownload') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 2
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
centrs = [f(cluster) for cluster in clusters if len(cluster)>100]
tx = sum(centr[0] for centr in centrs)/len(centrs)
ty = sum(centr[1] for centr in centrs)/ len(centrs)
print(tx*10000, ty*10000)



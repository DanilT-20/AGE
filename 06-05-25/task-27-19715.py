from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27.21.A_19715.txt') as file:
    data = [list(map(float, s.replace(',','.').split())) for s in file]
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
centers = [f(cluster) for cluster in clusters if len(cluster)>100]
print(int(sum(centr[0] for centr in centers)/len(centers)*10000),
      int(sum(centr[1] for centr in centers)/len(centers)*10000))
with open('27.21.B_19715.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 4
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
print(int(sum(c[0] for c in centrs)/len(centrs)*10000), int(sum(c[1] for c in centrs)/len(centrs)*10000))


from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist+= dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27_B_21720.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]
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
print([len(cluster) for cluster in clusters])
centers = [f(cluster) for cluster in clusters]
px = sum(centr[0] for centr in centers)/len(centers)
py = sum(centr[1] for centr in centers)/len(centers)
print(int(px*10000), int(py*10000))




from math import dist
def f(cl):
    distance = []
    for dot4 in cl:
        sum_dist = 0
        for dot3 in cl:
            sum_dist += dist(dot4, dot3)
        distance.append([sum_dist, dot4])
    return min(distance)[1]
with open('27_B_21911.txt')as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]
clusters = []
eps = 2
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2)<eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
centers = [f(cl) for cl in clusters]
px = sum(center[0] for center in centers)/len(centers)
py = sum(center[1] for center in centers)/len(centers)

print(int(px*10000), int(py*10000))


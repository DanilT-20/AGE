from math import dist
def f(cl):
    distance = []
    for dot4 in cl:
        sum_dist = 0
        for dot3 in cl:
            sum_dist += dist(dot4, dot3)
        distance.append([sum_dist, dot4])
    return min(distance)[1]
with open('27_A_21932.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]
eps = 2
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
print([(len(cluster), f(cluster)) for cluster in clusters])
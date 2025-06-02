def dist(dot1, dot2):
    return max(abs(dot1[0]-dot2[0]), abs(dot1[1]-dot2[1]))
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27.3.A_19891.txt') as file:
    cl1 = []
    cl2 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if x <3:
            cl1.append([x, y])
        if x>3:
            cl2.append([x, y])
centr1 = f(cl1)
centr2 = f(cl2)
px = (centr1[0]+centr2[0])/2
py = (centr1[1]+centr2[1])/2
print(int(px*10000), int(py*10000))
with open('27.3.B_19891.txt') as file:
    data = [list(map(float, s.replace(',', '.').split())) for s in file]
eps = 0.3
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
px = sum(centr[0] for centr in centrs)/len(centrs)
py = sum(centr[1] for centr in centrs)/ len(centrs)
print(int(px*10000), int(py*10000))

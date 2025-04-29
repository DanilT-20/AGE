from math import dist
def centroid(cl):
    distance = []
    for dot in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_17882.txt') as file:
    cl1 = []
    cl2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 1:
            cl1.append([x, y])
        else: cl2.append([x, y])
center1 = centroid(cl1)
center2 = centroid(cl2)
px = (center1[0] + center2[0])/2
py = (center1[1] + center2[1])/2
print(int(px*10000), int(py * 10000))


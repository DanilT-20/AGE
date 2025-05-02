from math import dist
def centroid(claster):
    distance = []
    for dot1 in claster:
        sum_dist = 0
        for dot2 in claster:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]


with open('27_B_17882.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 5 and y >4:
            cl1.append([x, y])
        if x > 5:
            cl2.append([x, y])
        if x < 5 and y < 4:
            cl3.append([x, y])
centr1 = centroid(cl1)
centr2 = centroid(cl2)
centr3 = centroid(cl3)

px = (centr1[0] + centr2[0]+ centr3[0])/3
py = (centr1[1] + centr2[1] + centr3[1])/3
print(int(px*10000), int(py*10000))
from math import dist
def centroid(lc):
    distance = []
    for dot1 in lc:
        sum_dist = 0
        for dot2 in lc:
            sum_dist+= dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27_A_20816.txt') as file:
    cl1 = []
    cl2 = []
    for i in file:
        i = str(i).replace(',', '.')
        x, y = map(float, i.split())
        if y > 0:
            cl1.append([x, y])
        else: cl2.append([x,y])
centr1 = centroid(cl1)
centr2 = centroid(cl2)
px = (centr1[0] + centr2[0])/2
py = (centr1[1] + centr2[1])/2
print(px*10000, py*10000)


with open('27_B_20816.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        i = str(i).replace(',', '.')
        x, y = map(float, i.split())
        if x > -5 and y > -5:
            cl1.append([x,y])
        if x < -5:
            cl2.append([x,y])
        if x > -5 and y < -5:
            cl3.append([x, y])
centr1 = centroid(cl1)
centr2 = centroid(cl2)
centr3 = centroid(cl3)
px = (centr1[0] + centr2[0]+centr3[0])/3
py = (centr1[1]+centr2[1]+centr3[1])/3
print(px*10000, py*10000)
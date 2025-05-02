from math import dist
def f(cl):
    distance=[]
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27_A_17916.txt') as file:
    cl1 = []
    cl2 = []
    for i in file:
        i = str(i).replace(',', '.')
        x, y = map(float, i.split())
        if y > 8:
            cl1.append([x, y])
        if y < 8:
            cl2.append([x,y])
centr1 = f(cl1)
centr2 = f(cl2)
px = (centr1[0]+centr2[0])/2
py = (centr1[1]+centr2[1])/2
print(px*10000, py*10000)


with open('27_B_17916.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    for i in file:
        i = i.replace(',', '.')
        x, y = map(float, i.split())
        if y>14:
            cl1.append([x, y])
        if y > 10 and y < 14:
            cl2.append([x, y])
        if y > 6 and y < 10:
            cl3.append([x, y])
        if y <5 and x < 8:
            cl4.append([x, y])
        if x > 12:
            cl5.append([x, y])
centr1 = f(cl1)
centr2 = f(cl2)
centr3 = f(cl3)
centr4 = f(cl4)
centr5 = f(cl5)
px = (centr1[0]+centr2[0]+centr3[0]+centr4[0]+centr5[0])/5
py = (centr1[1]+centr2[1]+centr3[1]+centr4[1]+centr5[1])/5
print(px*10000, py*10000)

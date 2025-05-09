from math import dist
def f(cl):
    distance = []
    for dot1 in cl:
        sum_dist = 0
        for dot2 in cl:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
with open('27_A_21599.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if y > x-10:
            cl1.append([x, y])
        elif y < 5:
            cl2.append([x, y])
        else:
            cl3.append([x, y])
centr1 = f(cl1)
centr2 = f(cl2)
centr3 = f(cl3)
px = (centr1[0]+centr2[0]+centr3[0])/3
py = (centr1[1]+centr2[1]+centr3[1])/3
print(int(px*10000), int(py*10000))
with open('27_B_21599.txt') as file:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    cl6 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if y < -2*x - 26 :
            cl1.append([x, y])
        elif y > -2*x - 26 and x < 10:
            cl2.append([x, y])
        elif x > -10 and y > int(24/13*100)/100*x-int(24*7/13*100)/100:
            cl3.append([x, y])
        elif y < int(24/13*100)/100*x-int(24*7/13*100)/100 and y > :
            cl4.append([x, y])
        elif :
            cl5.append([x, y])
        else:
            cl6.append([x, y])
print(len(cl1), len(cl2), len(cl3), len(cl4), len(cl5), len(cl6))
centr1 = f(cl1)
centr2 = f(cl2)
centr3 = f(cl3)
centr4 = f(cl4)
centr5 = f(cl5)
centr6 = f(cl6)
px = (centr1[0]+centr2[0]+centr3[0]+centr4[0]+centr5[0] +centr6[0])/6
py = (centr1[1]+centr2[1]+centr3[1]+centr4[1]+centr5[1] +centr6[1])/6
print(int(px*10000), int(py*10000))


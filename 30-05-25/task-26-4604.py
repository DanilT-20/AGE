with open('26_4604.txt') as file:
    N = int(file.readline())
    lenn = [int(i) for i in file]
lenn = sorted(lenn[1:])[::-1]
minn = [lenn[0]]
for i in lenn:
    if minn[-1] - i >= 3:
        minn.append(i)
print(len(minn), minn[-1])
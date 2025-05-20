with open('24_19489.txt') as file:
    data = file.readline()
data = data.replace('WSFWW', 'WSFW SFWW').split()
dat = []
for i in data:
    if i.count('WWF')<=120:
        dat.append(i)
print(len(max(data, key=len)), len(max(dat, key=len)))
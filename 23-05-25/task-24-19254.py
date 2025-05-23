with open('24_19254.txt') as file:
    data = file.readline()
maxx = 0
data = data.split('FSRQ')
for i in range(len(data)-80):
    dat = data[i:i+81]
    dat = 'FSRQ'.join(dat)
    maxx = max(len(dat), maxx)
print(maxx+6)
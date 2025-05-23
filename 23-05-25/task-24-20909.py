with open('24_20909.txt') as file:
    data = file.readline()
maxx = 0
data = data.split('AB')
for i in range(len(data)-100):
    dat = data[i:i+101]
    dat = 'AB'.join(dat)
    maxx = max(len(dat), maxx)
print(maxx+2)
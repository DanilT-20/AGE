with open('24_21717.txt') as file:
    data = file.readline()
minn = 100000
data = data.split('RSQ')
for i in range(len(data)-129):
    dat = data[i:i+130]
    dat = 'RSQ'.join(dat)
    minn = min(minn, len(dat))
print(minn+4)

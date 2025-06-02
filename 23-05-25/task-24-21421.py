from string import ascii_uppercase
maxx = 0
with open('24_21421.txt') as file:
    data = file.readline()
for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')
data = data.split()
for i in data:
    for n in range(len(i)):
        for y in range(n, len(i)):
            u = i[n:y+1]
            if u[0]!='0' and int(u[-1], 12)%2==0:
                maxx = max(len(u), maxx)
print(maxx)

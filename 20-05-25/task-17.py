with open('17_5882.txt') as file:
    data = [int(s) for s in file]
dat = []
for i in range(len(data)-1):
    u = data[i:i+2]
    if len([i for i in u if str(i)[-1]=='3']) == 1:
        dat.append(min(u))
summ = sum([int(i)**2 for i in str(abs(min(dat)))])
dat1 = [i for i in data if str(i).count('3')>0 and i >= summ]
print(min(dat1), len(dat1))

with open('24_19751.txt') as file:
    data = file.readline()

ans = []
for i1 in range(len(data) - 1):
    i11 = data[i1]
    if i11 == 'A':
        for i2 in range(i1 + 1, len(data)):
            i22 = data[i2]
            if i22 in '-*BCDA':
                data1 = data[i1 + 1:i2].strip('+')
                if data1 and '++' not in data1:
                    ans.append([sum(map(int, data1.split('+'))), len(data1) + 1])
                break
print(max(ans))
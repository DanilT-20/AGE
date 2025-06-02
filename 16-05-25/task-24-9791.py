from string import ascii_uppercase

with open('24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')
data = data.split()
ans = 0
for i in data:
    i = i.lstrip('0')
    if int(i, 16):
        ans = max(ans,len(i))
    else:
        for l in range(len(data)):
            for i1 in range(len(data), l, -1):
                ps = i[l:i1].lstrip('0')
                if int(ps, 16)%6==0:
                    ans = max(ans, len(ps))
                    break

print(ans)



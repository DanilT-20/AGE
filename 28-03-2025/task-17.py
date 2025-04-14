with open('17_12735.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if str(i)[-2:] == '09')
for i in range(len(data)-2):
    u = data[i:i+3]
    if len([i for i in u if i%7==0]) == 2 and sum(u) < maxx:
        ans.append(u[0]*u[1]*u[2])
print(len(ans), min(ans))

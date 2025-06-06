with open('17_17680.txt') as file:
    data = [int(i) for i in file]
ans = []
minn = min(i for i in data if abs(i)%41==0 and i > 0)
for i in range(len(data)-1):
    u = data[i:i+2]
    if len(set(u)) == len(u) and abs(u[0] - u[1])%minn == 0:
        ans.append(sum(u))
print(len(ans), max(ans))

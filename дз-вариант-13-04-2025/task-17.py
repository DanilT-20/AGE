with open('17_6791.txt') as file:
    data = [int(i) for i in file]
ans = []
minn = min(i for i in data if str(i)[-2:] == '68')**2
for i in range(len(data)-1):
    u = data[i:i+2]
    if len([1 for n in u if str(n)[-2:] == '68']) == 1 and u[0]**2 + u[1]**2 >= minn:
        ans.append(u[0]**2 + u[1]**2)
print(len(ans), max(ans))

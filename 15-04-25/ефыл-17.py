with open('17_12249.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-1] == '3')
for i in range(len(data)-2):
    u = data[i:i+3]
    if len([i for i in u if str(i)[-1] == '3']) >= 1 and sum(u) <= maxx:
        ans.append(sum(u))
print(len(ans), max(ans))

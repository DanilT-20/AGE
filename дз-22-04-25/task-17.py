with open('17_2399.txt') as file:
    data = [int(i) for i in file]
ans = []
summ = sum(map(int, ''.join([str(i) for i in data if i % 35 == 0])))
for i in range(len(data)-1):
    u = data[i:i+2]
    if len([i for i in u if i > summ]) == 1:
        for x in u:
            if x != [i for i in u if i > summ][0] and hex(x)[-2:] == 'ef':
                ans.append(sum(u))
print(len(ans), min(ans))
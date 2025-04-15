with open('24_19149.txt') as file:
    data = file.readline()
ans = []
for i in range(len(data)):
    d1 = data[i]
    if d1 == '(':
        for x in range(i+1, len(data)):
            d2 = data[x]
            if d2 == '(':
                break
            if d2 == ')':
                if data[i+1]!='+' and data[x-1]!='+':
                    n = data[i+1:x]
                    j = n.split('+')
                    if '' not in j and sum(map(int,j))%2==0:
                        ans.append(len(n) + 2)
                break
print(max(ans))

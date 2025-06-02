from re import *
with open('24_17641.txt') as file:
    data = file.readline()
p1 = r'([1-9][0-9]*|0)'
pattern = fr'({p1}[*+])+{p1}'

match = finditer(pattern, data)
match = [match.group() for match in match]
ans = 0
for matc in match:
    if eval(matc) == 0:
        ans = max(ans, len(matc))
    else:
        for i in range(len(matc)+1):
            for r in range(len(matc), i, -1):
                sub_str = matc[i:r].strip('+*')
                if len(sub_str)<2:
                    break
                if sub_str[0] == '0' and sub_str[1] in '0123456789':
                    continue
                if eval(sub_str)==0:
                    ans = max(ans, len(sub_str))
                    break
print(ans)
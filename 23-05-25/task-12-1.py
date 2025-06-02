from re import *
with open('24_6798.txt') as file:
    data = file.readline()

pattern = r'([CDF][ACDFO].[AO])+'

matches = finditer(pattern, data)
matches = [match.groups() for match in matches]

print(len(max(matches, key=len))//3)
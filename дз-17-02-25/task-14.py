count = 0
num = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
while num:
    if num % 25 == 0:
        count += 1
    num //= 25
print(count)
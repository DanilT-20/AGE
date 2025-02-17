from string import ascii_uppercase, digits
alph = digits + ascii_uppercase
def f(n, s):
    res = ''
    while n:
        res += alph[n % s]
        n //= s
    return res[::-1]
maxx = 0
num = f(3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 2*15**74 + 3, 15)
for i in alph[:15]:
    num1 = num
    for x in alph[:15]:
        if x != i:
            num1 = num1.replace(x, '*')
    num1 = num1.split('*')
    if maxx < len(max(num1, key=len)):
        maxx = len(max(num1))
print(maxx)

def f(num):
    res = set()
    for i in range(1, int(num**0.5)+1):
        if num %i == 0:
            res|={i, num//i}
    if len(res) == 2:
        return 1
    return 0
ans = []
for n in range(4, 1000):
    st = '>' + 25*'0'+n*'1'+25*'2'
    while '>1' in st or '>2' in st or '>0' in st:
        if '>1' in st:
            st = st.replace('>1', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '1>', 1)
    st = st.replace('>', '')
    summ = sum(map(int,st))
    if f(summ):
        ans.append(n)
print(min(ans))


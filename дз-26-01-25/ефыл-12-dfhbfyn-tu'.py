for n in range(1, 10000):
    st = '>' + '0'*21 + n*'1' + '2'*11
    while '>1' in st or '>2' in st or '>0' in st:
        if '>1' in st:
            st = st.replace('>1', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '1>', 1)
    st = st.split('>')
    st = ''.join(st)
    if sum(map(int, st)) % n == 0:
        print(n)
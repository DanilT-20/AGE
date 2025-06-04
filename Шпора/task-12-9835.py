for n in range(4, 10001):
    st = '1' + '8'*n
    while '18' in st or '388' in st or '888' in st:
        if '18' in st:
            st = st.replace('18', '8', 1)
        if '388' in st:
            st = st.replace('388', '81', 1)
        if '888' in st: st = st.replace('888', '3', 1)
    if st.count('1') == 3:
        print(n)
        break

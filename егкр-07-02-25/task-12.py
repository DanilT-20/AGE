st = '>' + 10*'357'
while '>3' in st or '>5' in st or '>7' in st:
    if '>3' in st:
        st = st.replace('>3', '55>', 1)
    if '>5' in st:
        st = st.replace('>5', '5>3', 1)
    if '>7' in st:
        st = st.replace('>7', '3>5', 1)
st = st.split('>')
st = ''.join(st)
summ = sum(map(int, st))
print(summ)
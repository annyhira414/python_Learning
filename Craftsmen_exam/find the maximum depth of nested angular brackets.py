def maxDepth(s):
    count = 0
    st = []
    for i in range(len(s)):
        if s[i] == '<':
            st.append(i)
        elif s[i] == '>':
            if count < len(st):
                count = len(st)
            st.pop()

    return count
s = "<<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>><<<<<<<<<<<>>>>>>"
print(maxDepth(s))
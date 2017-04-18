def braces(self, A):
    if not A:
        return 0
    st = list()
    for letter in A:
        if letter != ")":
            st.append(letter)
        else:
            c = 0
            while st[-1] != "(":
                c += 1
                st.pop()
            st.pop()
            if c == 0 or c == 1:
                return 1
    return 0
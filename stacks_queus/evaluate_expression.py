def returnExpr(a, b, op):
    a, b = int(a), int(b)
    if op == "+":
        return a + b
    elif op == "-":
        print a, b, a-b
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b


def evalRPN(A):
    st = list()
    for let in A:
        print st
        if let not in ("+", "-", "*", "/"):
            if let in ("(", ")", "[", "]", "{", "}"):
                continue
            else:
                st.append(let)
        else:
            sec = st.pop()
            fst = st.pop()
            st.append(returnExpr(fst, sec, let))
    return st[-1]

A = [ "5", "1", "2", "+", "4", "*", "+", "3", "-" ]
A = ["4", "2", "-"]
print evalRPN(A)
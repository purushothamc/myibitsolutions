def inorderTraversal(A):
    result, output = list(), list()
    if not A:
        return result
    done, current = False, A
    while not done:
        if current:
            result.append(current)
            current = current.left
        else:
            if result:
                popped = result.pop()
                output.append(popped.val)
                current = popped.right
            else:
                done = True
    return output
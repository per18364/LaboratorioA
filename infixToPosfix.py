def infix_to_postfix(infix):
    precedence = {'*': 3, '.': 2, '|': 1, '(': 0}
    stack = []
    postfix = ''
    for symbol in infix:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        elif symbol in precedence:
            while stack and precedence[stack[-1]] >= precedence[symbol]:
                postfix += stack.pop()
            stack.append(symbol)
        else:
            postfix += symbol
    while stack:
        postfix += stack.pop()
    return postfix

# '+': 5, '?': 4,

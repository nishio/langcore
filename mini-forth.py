# -*- enoding: utf-8 -*-
"""
mini-Forth
Forth解説のための最小限のForth実装
"""

data = "1 2 + 3 * print"
tokens = data.split()
stack = []
cur = 0
while cur < len(tokens):
    if t in "123":
        stack.append(int(t))

    elif t == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y)

    elif t == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y)

    elif t == "print":
        x = stack.pop()
        print "print:", x

    else:
        raise NotImplementedError(t)



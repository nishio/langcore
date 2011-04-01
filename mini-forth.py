# -*- enoding: utf-8 -*-
"""
mini-Forth
Forth解説のための最小限のForth実装
"""

data = ": dp dup print ; 1 2 dp + 3 * print"
tokens = data.split()
stack = []
words = {}

def evaluate(tokens):
    print "eval", tokens
    cur = 0
    while cur < len(tokens):
        t = tokens[cur]
        cur += 1
        prevstack = stack[:]
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
        elif t == "dup":
            x = stack.pop()
            stack.append(x)
            stack.append(x)
        elif t == ":":
            buf = []
            while True:
                t = tokens[cur]
                cur += 1
                if t == ";": break
                buf.append(t)
            words[buf[0]] = buf[1:]

        elif words.has_key(t):
            evaluate(words[t])
        else:
            raise NotImplementedError(t)

        print "%s->(%s)->%s" % (prevstack, t, stack)


evaluate(tokens)
print words

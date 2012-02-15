import parser
import symbol
import token
import ast
import compiler
import json

def _code2st(code):
    return parser.expr(code).totuple()


def _st2json(st):
    if isinstance(st, tuple):
        return map(_st2json, st)
    else:
        leaf = symbol.sym_name.get(st, st)
        return token.tok_name.get(leaf, leaf)


def get_st(code):
    return json.dumps(_st2json(_code2st(code)))


def code2ast(code):
    return ast.parse(code)


def _obj(name, **kw):
    "utility to make dict"
    kw["name"] = name
    return kw


def ast2json(ast):
    global t
    name = ast.__class__.__name__
    print name
    if name == "Module":
        return _obj(name, body=map(ast2json, ast.body))
        
    elif name == "Expr":
        # col_offset, lineno
        return _obj(name, value=ast2json(ast.value))

    elif name == "BinOp":
        # col_offset, lineno
        op = ast.op.__class__.__name__
        left = ast2json(ast.left)
        right = ast2json(ast.right)
        return _obj(name, op=op, left=left, right=right)

    elif name == "Num":
        # col_offset, lineno
        n = ast.n
        return _obj(name, n=n)

    else:
        t = ast
        raise NotImplementerError
        


def code2bc(code):
    try:
        bc = compiler.compile(code, "<file>", "eval")
    except SyntaxError:
        try:
            bc = compiler.compile(code, "<file>", "exec")
        except SyntaxError, e:
            raise



def test():
    global t
    print get_st("1 + 1")
    t = ast2json(code2ast("1 + 1"))
    print t


if __name__ == "__main__":
    test()

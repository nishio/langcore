# -*- encoding: utf-8 -*-
"""
mini-VM 解説のための最小限のVM
最小限のサブルーチン呼び出し
・帰るアドレスはmem[5]に決め打ちで保管
　→つまり呼び出しをネストできない
　→ネストするにはどうすればいい？→スタック
・返り値はmem[0]に入る
・引数？なにそれ？
　→呼び出し元とみえているものが同じ
　　書き換えれば呼び出し元にも波及
　→この問題の解決方法は動的スコープのところでやる

jump pos : PCをposに変更
if_eq a1 v1 pos : mem[a1] == v1 ならjump pos
print a1 : mem[a1]をprint
set a1 v1 : mem[a1]をv1にする
sub v1 : mem[0]からv1を引く
"""

memory = [0] * 10
RETURN_ADDR = 5 # returnする場所を格納しておく番地

# maxの実装
code = [
    ("set", 1, 10),      # B = 10
    ("set", 2, 20),      # C = 20
    ("call", 8),         # call max(B, C)
    ("print", 0),        # print A
    ("set", 1, 30),      # B = 30
    ("call", 8),         # call max(B, C)
    ("print", 0),        # print A
    ("jump", 999),       # goto end
    ("if_gt", 1, 2, 10), # 9: (subroutine max)
    ("return", 2),       # return C
    ("return", 1),       # return B
]

def eval(code):
    cur = 0
    while cur < len(code):
        line = code[cur]
        cur += 1
        op = line[0]
        if op == "set":
            memory[line[1]] = line[2]
        elif op == "print":
            print memory[line[1]]

        elif op == "if_eq":
            if memory[0] == line[1]:
                cur = line[2]

        elif op == "if_gt":
            print memory, line
            if memory[line[1]] > memory[line[2]]:
                cur = line[3]

        elif op == "sub":
            memory[0] -= line[1]

        elif op == "jump":
            cur = line[1]

        elif op == "return":
            ret = memory[RETURN_ADDR]
            cur = ret
            memory[0] = memory[line[1]]

        elif op == "call":
            memory[RETURN_ADDR] = cur # +1でないのはすでに上で1進めているから
            cur = line[1]

        else:
            raise NotImplementedError(op)


eval(code)


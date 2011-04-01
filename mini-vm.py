# -*- encoding: utf-8 -*-
"""
mini-VM 解説のための最小限のVM
最小限とは？最小限である必要があるか？
チューリング完全である必要があるのか？

jump pos : PCをposに変更
if_eq a1 v1 pos : mem[a1] == v1 ならjump pos
print a1 : mem[a1]をprint
set a1 v1 : mem[a1]をv1にする
sub v1 : mem[0]からv1を引く
"""

memory = [0] * 100
memory[50] = 51
# 50をスタックの頭を指す値, 51を指している
# 51からがスタック
# 0を返り値
# 40からが引数

# maxの実装
code = [
    ("set", 0, 10),  # A = 10
    ("if_eq", 0, 5), # 1: if A == 0 goto 5
    ("sub", 1),      # A = A - 1

    ("print", 0),    # print A
    ("jump", 1),     # 5: goto 1

    ("if_gt", 1, 2, ??),
    ("return", 2),
    ("return", 1),
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
            if memory[0] > line[1]:
                cur = line[2]
        elif op == "sub":
            memory[0] -= line[1]
        elif op == "jump":
            cur = line[1]
        elif op == "return":
            esp = memory[50] # TODO 名前
            ret = memory[esp]
            cur = ret
            memory[0] = memory[line[1]]
        elif op == "call":
            memory[50] += 1 # TODO 名前
            memory[memory[50]] = cur + 1
            cur = line[1]
            
        else:
            raise NotImplementedError
eval(code)


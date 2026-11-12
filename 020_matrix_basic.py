# -*- coding: utf-8 -*-
# 020_matrix_basic.py —— 二维数组：读矩阵、行和、总和（2026-11-07）
#
# ⚠️ 【2026-11-11 补记 · 本题设计失败，别当二维数组练过】
#   用户指出：这题不用矩阵也能做 —— 每行 sum 一下就扔，a 只被遍历一次。
#   实测确认：存储、a[i][j] 双下标、初始化陷阱，三样一个都没练到。
#   判据：**能一边读一边算完的题，就不需要矩阵。**
#   真正的二维数组练习见 `026_matrix_transpose.py`（矩阵转置，必须存）。
#   本题保留仅作"读入多行"的练习。
#
# 这是 L1 缺口第 1 项：二维数组。
# 初始化的坑（[[0]*m]*n）昨天已经讲过，今天练「用」：
#   读入、遍历、a[i][j] 是什么意思。
#
# 规则：从空文件开始写。不许看 017、019。
#
# 用法：
#   python 020_matrix_basic.py


import io
import sys


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】矩阵的行和与总和
#
#   读入一个 n 行 m 列的矩阵，输出 n + 1 行：
#     第 1 ~ n 行：每一行的 n 个数之和（按行的顺序）
#     第 n + 1 行：所有数的总和
#
# 【输入】
#   第 1 行：n m
#   接下来 n 行：每行 m 个整数（空格分隔）
#
# 【输出】n + 1 行
#
# 【样例】
#   输入            输出
#   2 3             6
#   1 2 3           15
#   4 5 6           21
#
#   （第 1 行 1+2+3=6，第 2 行 4+5+6=15，总和 21）
#
# 【提示】
#   ① 读矩阵：外层循环 n 次，每次 input().split() 拿一行，
#      转成 int 列表 append 进去。
#   ② a[i][j] 是第 i 行第 j 列。行数 = len(a)，列数 = len(a[0])。
#   ③ 初始化矩阵用列表推导式：
#         [[0] * m for _ in range(n)]
#      千万别用 [[0] * m] * n —— 那是 n 份引用指向同一个列表，
#      改一个格子会一整列跟着变。
# ----------------------------------------------------------------------
# 在下面的函数里写：
# ----------------------------------------------------------------------

def solve():
    n,m=map(int,input().split())
    a=[]
    b=0
    for i in range(n):
        data=list(map(int,input().split()))
        a.append(data)
    for s in a:
        res=sum(s)
        print(res)
        b+=res
    print(b)




# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    ("2 3\n1 2 3\n4 5 6\n", "6\n15\n21"),
    ("1 1\n7\n", "7\n7"),
    ("3 1\n1\n2\n3\n", "1\n2\n3\n6"),
    ("2 2\n-1 -1\n-1 -1\n", "-2\n-2\n-4"),
    ("2 4\n1 2 3 4\n5 6 7 8\n", "10\n26\n36"),
]


def self_check():
    ok = 0
    for i, (fake_input, expected) in enumerate(CHECKS, 1):
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(fake_input)
        buf = io.StringIO()
        sys.stdout = buf
        err = None
        try:
            solve()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        finally:
            sys.stdin, sys.stdout = old_in, old_out

        if err:
            print(f"  用例 {i}  x 报错 -> {err}")
            continue

        actual = buf.getvalue().replace("\r\n", "\n").rstrip("\n")
        exp = expected.rstrip("\n")
        if actual == exp:
            ok += 1
            print(f"  用例 {i}  ✓ 通过")
        else:
            print(f"  用例 {i}  ✗ 未过")
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {exp!r}")
            print(f"       实际: {actual!r}")

    print()
    print(f"总计 {ok} / {len(CHECKS)}")


if __name__ == "__main__":
    self_check()

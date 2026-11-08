# -*- coding: utf-8 -*-
# 022_gcd_recursive.py —— 递归入门：gcd + lcm（2026-11-07）
#
# L1 缺口第 4 项：递归。
#
# 递归三要素（缺一个就死循环或算错）：
#   ① 出口：什么时候停
#   ② 推进：每次调用离出口更近
#   ③ 合并：怎么用子问题的答案
#
# gcd 的递归定义（欧几里得算法）：
#   gcd(a, b) = gcd(b, a % b)    当 b ≠ 0
#   gcd(a, 0) = a                出口
#
# 用法：
#   python 022_gcd_recursive.py


import io
import sys


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】最大公约数与最小公倍数
#
#   读入两个正整数 a b，输出两行：
#     第 1 行：a 和 b 的最大公约数（gcd）
#     第 2 行：a 和 b 的最小公倍数（lcm）
#
#   lcm 的公式：lcm = a * b // gcd
#
# 【输入】一行：a b
# 【输出】两行：gcd 和 lcm
#
# 【样例】
#   输入      输出
#   12 8      4
#             24
#
# 【要求】
#   gcd 必须用**递归**实现，不许用 while 循环版。
#   递归三要素自查：
#     ① 出口在哪？条件是什么？
#     ② 每次递归，哪个参数在变小？
#     ③ 返回值怎么合并？
#
# ----------------------------------------------------------------------
# 在下面的函数里写：
# ----------------------------------------------------------------------

def solve():
    a,b=map(int,input().split())
    x,y=a,b
    def gongyueshu(a,b):
        y=a%b
        if y==0:
            return b
        return gongyueshu(b,y)
    gcm=gongyueshu(a,b)
    print(gcm)
    lcm=x*y//gcm
    print(lcm)



# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    ("12 8\n", "4\n24"),
    ("100 75\n", "25\n300"),
    ("7 13\n", "1\n91"),
    ("5 5\n", "5\n5"),
    ("1 100\n", "1\n100"),
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

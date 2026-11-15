# -*- coding: utf-8 -*-
# 028_diff_minmax.py —— 复习：差分 + 打擂台（2026-11-13 周五加练）
#
# 为什么是这道：
#   「差分」你学过（016/017/019/023），「打擂台」你学过（R3/R7/V2），
#   但两样从来没在**同一道题**里用过。分开会做 ≠ 合起来会写。
#
# 这题的合体点在 restore：
#   还原前缀和的时候，每算出一个 a[i]，就顺手跟擂主比一次 ——
#   不需要把整个数组存下来，也不需要事后再 max 一遍。
#
# 三个坑，都在你已经踩过的地方：
#   ① d 要开多大（023 的坑：r = n 时 d[r+1] 会摸边界）
#   ② 初值给几（R7 的坑：min 和 max 的初值不是同一个数）
#   ③ 别先攒再算（攒了 5 次的坑）
#
# 用法：
#   python 028_diff_minmax.py

import io
import sys


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】区间加完之后，最大和最小是多少
#
#   给 n 个数，再做 m 次「区间加」操作：每次把下标 l 到 r（含两端）
#   的每个数加上 x。全部操作做完之后，输出最终的**最大值**和**最小值**。
#
#   ⚠️ 不需要输出数组本身，只要这两个数。
#
# 【输入】
#   第 1 行：n
#   第 2 行：n 个整数
#   第 3 行：m
#   之后 m 行：每行 3 个整数 l r x
#   （下标 l、r 从 1 开始数；m 可能是 0，此时没有后面那些行）
#
# 【输出】一行，两个整数：最大值 最小值
#
# 【例】
#   输入                输出
#   5                   11 -1
#   1 2 3 4 5
#   2
#   1 3 10
#   2 5 -5
#
#   验算： [1,2,3,4,5]
#          +10 到 1~3 → [11,12,13,4,5]
#           -5 到 2~5 → [11,7,8,-1,0]
#           最大 11，最小 -1
#
# 【硬要求】
#   1. **必须用差分**，不许每行操作都去循环改数组
#   2. **还原的时候顺便打擂台** —— 每算出一个 a[i] 就比一次，
#      不许先把整个数组还原出来再 max()/min()
#   3. 不许用 max() / min()
#
# 【提示】
#   ① 三个模板函数还要不要？哪些还需要，哪些不需要？（这题不输出数组）
#   ② 最大和最小的初值，能是同一个数吗？
#   ③ d 数组要开多大？（想想 r 最大能到几）
#
# ----------------------------------------------------------------------
# 在下面的函数里写：
# ----------------------------------------------------------------------

def solve():
    n=int(input())
    da=list(map(int,input().split()))
    a=[0]+da
    def build_diff(a,n):
        d=[0]*(n+2)
        for i in range(1,n+1):
            d[i]=a[i]-a[i-1]
        return d
    d=build_diff(a,n)
    m=int(input())
    def range_add(d,l,r,x):
        d[l]+=x
        d[r+1]-=x
    for h in range(m):
        l,r,x=map(int,input().split())
        range_add(d,l,r,x)

    def restore(d,n):
        a=[0]*(n+1)
        res=0
        max_a = -float('inf')
        min_a = float('inf')
        for i in range(1,n+1):
            res+=d[i]
            a[i]=res
            if a[i] > max_a:
                max_a = a[i]
            if a[i] < min_a:
                min_a = a[i]
        return min_a,max_a

    min_a, max_a=restore(d,n)
    print(max_a,min_a)



# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    # 样例
    ("5\n1 2 3 4 5\n2\n1 3 10\n2 5 -5\n", "11 -1"),
    # m = 0：一次操作都没有，直接取原数组的最值
    ("3\n5 5 5\n0\n", "5 5"),
    # 单元素，加负数 → 全负
    ("1\n7\n1\n1 1 -10\n", "-3 -3"),
    # 全负数，全体加同一个正数
    ("4\n-1 -2 -3 -4\n1\n1 4 5\n", "4 1"),
    # 全 0，加 0（最无聊的用例，专抓初值写错）
    ("2\n0 0\n1\n1 1 0\n", "0 0"),
    # r = n（摸 d[r+1] 边界）+ 最大值落在最后
    ("4\n1 1 1 1\n1\n4 4 9\n", "10 1"),
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

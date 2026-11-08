# -*- coding: utf-8 -*-
# 019_diff_from_scratch.py —— 从零写一道完整的差分题（2026-11-05）
#
# 这一天不给你模板、不给骨架、不给提示。
#
# 规则：
#   1. **不许打开 `016_difference.py` 和 `017_difference_drill.py`**。
#      里面就是答案，看了等于没写。
#   2. 从 `input()` 开始，一直到 `print()`，全部自己写。
#   3. 跑自检，5 个用例全过才算过。
#
# 这不是"再练一遍模板"，这是**检验你能不能从空文件走到跑通**。
# 昨天 T1 那次卡了 3 处（占位 0、返回值、循环位置），全在流程上，不在模板上。
#
# 用法：
#   python 019_diff_from_scratch.py


import io
import sys


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】区间加分
#
#   有 n 个学生，第 i 个学生当前的分数是 a[i]。
#   老师要做 m 次加分：每次给学号 l 到 r 的学生**每人加 x 分**。
#   所有操作做完后，输出两行：
#     第 1 行：每个学生的最终分数，按学号从小到大，空格分隔
#     第 2 行：全体学生的**总分**
#
# 【输入】
#   第 1 行：n m
#   第 2 行：n 个整数 a[1] a[2] ... a[n]
#   接下来 m 行：每行三个整数 l r x
#
# 【输出】两行，见上
#
# 【样例】
#   输入                输出
#   5 2                 13 13 16 13 15
#   3 1 4 1 5           70
#   2 4 2
#   1 5 10
#
#   （先给 2~4 号各加 2 分 → 3 3 6 3 5；
#     再给全班各加 10 分 → 13 13 16 13 15；总分 70）
#
# 【数据规模】n, m 最大到 2×10^5，所以每次操作不能真去挨个加。
#
# ----------------------------------------------------------------------
# 就在下面这个函数里写。函数名和自检已经对好了，别改。
# ----------------------------------------------------------------------

def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a=[0]+a
    def build_diff(a,n):
        d=[0]*(n+2)
        for i in range(1,n+1):
            d[i]=a[i]-a[i-1]
        return d

    d = build_diff(a, n)
    def range_add(d,l,r,x):
        d[l]+=x
        d[r+1]-=x
    for i in range(m):
        l,r,x=map(int,input().split())
        range_add(d,l,r,x)
    def restore(d,n):
        a=[0]*(n+1)
        cur=0
        for s in range(1,n+1):
            cur+=d[s]
            a[s]=cur
        return a


    a=restore(d,n)
    print(*a[1:])
    print(sum(a[1:]))



# ======================================================================
# 自检（别改这部分）
# ======================================================================

CHECKS = [
    ("5 2\n3 1 4 1 5\n2 4 2\n1 5 10\n", "13 13 16 13 15\n70"),
    ("3 1\n1 2 3\n1 1 5\n", "6 2 3\n11"),
    ("1 1\n7\n1 1 3\n", "10\n10"),
    ("4 2\n5 5 5 5\n1 4 -5\n2 2 100\n", "0 100 0 0\n100"),
    ("6 3\n1 1 1 1 1 1\n1 2 1\n3 4 2\n5 6 3\n", "2 2 3 3 4 4\n18"),
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
    if ok == len(CHECKS):
        print("\n从零到跑通，成了。差分这条线算过关。")


if __name__ == "__main__":
    self_check()

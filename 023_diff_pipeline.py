# -*- coding: utf-8 -*-
# 023_diff_pipeline.py —— 错题重做：差分的完整流程（2026-11-08）
#
# 来源：019 的「流程三错」回炉。11-05 那天三个模板函数全对，
#       错的全在接缝处 —— 读入解包 / 传参顺序 / 中间搬运 / 输出切片。
#       所以这次不考「模板会不会背」，考「一条流水线能不能一次走通」。
#
# 和 019 的区别（三处刻意加难）：
#   ① 输入是多行混合的：第一行 n，第二行数组，第三行 m，之后 m 行操作
#   ② 操作的下标 l r 是 **1 开始** 的（题目这么给），而 Python 是 0 开始
#   ③ r 可以等于 n，所以 d[r+1] 会摸到边界
#
# 用法：
#   python 023_diff_pipeline.py


import io
import sys
from operator import is_not


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】区间加法（完整流水线）
#
#   输入格式：
#     第 1 行：n              数组长度
#     第 2 行：n 个整数        数组初始值
#     第 3 行：m              操作次数
#     之后 m 行：每行 l r x    把下标 l 到 r（含两端）每个数加 x
#
#   注意：这里的 l、r 是 **从 1 开始数** 的（题目惯例），
#         l=1 指的是数组第一个元素。
#
#   输出：一行，n 个数，空格隔开，是全部操作完成后的数组。
#
# 【样例】
#   输入                输出
#   5                   5 2 5 10 4
#   3 1 4 1 5
#   3
#   1 3 2
#   2 5 -1
#   4 4 10
#
#   验算：  [3,1,4,1,5]
#           +2 到 1~3 → [5,3,6,1,5]
#           -1 到 2~5 → [5,2,5,0,4]
#          +10 到 4~4 → [5,2,5,10,4]   ✓
#
# 【要求】
#   1. 必须用差分做，不许每行操作都去循环改 a（那是最慢的做法，白学差分）
#   2. 三个函数自己写全：build_diff / range_add / restore
#   3. 想清楚一件事：d 数组要开多大？
#      （提示只有这一句：涉及 d[r+1]）
#
# ----------------------------------------------------------------------
# 在下面的函数里写：
# ----------------------------------------------------------------------

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    a=[0]+arr
    m=int(input())
    def build_diff(a,n):
        d=[0]*(n+2)
        for i in range(1,n+1):
            d[i]=a[i]-a[i-1]
        return d
    d=build_diff(a,n)
    def range_add(d,l,r,x):
        d[l]+=x
        d[r+1]-=x
    for x in range(m):
        l,r,x=map(int,input().split())
        range_add(d,l,r,x)
    def restore(d,n):
        a=[0]*(n+1)
        res=0
        for x in range(1,n+1):
            res+=d[x]
            a[x]=res
        return a
    a=restore(d,n)
    print(*a[1:])



# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    # 样例
    ("5\n3 1 4 1 5\n3\n1 3 2\n2 5 -1\n4 4 10\n", "5 2 5 10 4"),
    # 单元素：l=r=n=1，两种边界同时出现
    ("1\n7\n2\n1 1 5\n1 1 -5\n", "7"),
    # 整段操作：r = n，d[r+1] 正好摸到 d[n+1]
    ("4\n1 2 3 4\n1\n1 4 100\n", "101 102 103 104"),
    # r = n 但不是 l = 1
    ("3\n10 20 30\n1\n2 3 5\n", "10 25 35"),
    # 两次全区间叠加，且初始值全 0
    ("6\n0 0 0 0 0 0\n2\n1 6 1\n1 6 1\n", "2 2 2 2 2 2"),
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
